"""
API Wrapper pour l'interface web
Centralise les appels aux fonctions backend
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add src to path
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))


class PortfolioReconstructor:
    """
    Wrapper pour la reconstruction de portefeuille
    """

    @staticmethod
    def reconstruct_ridge(alpha=1.0):
        """
        Reconstruction via Ridge Regression

        Returns:
            dict: {
                'weights': Series des pondérations,
                'r2': float,
                'correlation': float,
                'tracking_error': float,
                'timeseries': DataFrame avec tracking error temporel
            }
        """
        try:
            from reconstruction.fit_ridge_reconstruction import main as fit_ridge

            # Import paths avec chemin absolu
            from pathlib import Path

            # Get project root
            current_file = Path(__file__).resolve()
            project_root = current_file.parent.parent.parent.parent

            DATASET_PATH = project_root / "backend" / "datasets" / "wg_actions_reconstruction_dataset.csv"

            # Check if dataset exists
            if not DATASET_PATH.exists():
                return {
                    'error': f"Dataset not found: {DATASET_PATH}",
                    'weights': pd.Series(),
                    'r2': 0,
                    'correlation': 0,
                    'tracking_error': 0,
                    'timeseries': pd.DataFrame()
                }

            # Load and process
            df = pd.read_csv(DATASET_PATH, parse_dates=["Date"]).sort_values("Date")
            y = df["WG_RETURN"].values
            feature_cols = [c for c in df.columns if c not in ["Date", "WG_RETURN"]]
            X = df[feature_cols].values

            from sklearn.linear_model import Ridge
            from sklearn.preprocessing import StandardScaler
            from sklearn.pipeline import Pipeline
            from sklearn.metrics import r2_score

            model = Pipeline([
                ("scaler", StandardScaler(with_mean=True, with_std=True)),
                ("ridge", Ridge(alpha=alpha, fit_intercept=True))
            ])

            model.fit(X, y)
            y_hat = model.predict(X)

            r2 = r2_score(y, y_hat)
            resid = y - y_hat
            tracking_error = np.std(resid, ddof=1)
            corr = np.corrcoef(y, y_hat)[0, 1]

            ridge = model.named_steps["ridge"]
            coef = ridge.coef_
            weights = pd.Series(coef, index=feature_cols).sort_values(ascending=False)

            timeseries = pd.DataFrame({
                "Date": df["Date"],
                "WG_RETURN": y,
                "WG_REPL": y_hat,
                "residual": resid
            })

            return {
                'weights': weights,
                'r2': r2,
                'correlation': corr,
                'tracking_error': tracking_error,
                'timeseries': timeseries,
                'intercept': ridge.intercept_
            }

        except Exception as e:
            return {
                'error': str(e),
                'weights': pd.Series(),
                'r2': 0,
                'correlation': 0,
                'tracking_error': 0,
                'timeseries': pd.DataFrame()
            }

    @staticmethod
    def reconstruct_slsqp():
        """
        Reconstruction via SLSQP Optimization

        Returns:
            dict similaire à reconstruct_ridge
        """
        try:
            from scipy.optimize import minimize
            from pathlib import Path

            # Get project root
            current_file = Path(__file__).resolve()
            project_root = current_file.parent.parent.parent.parent

            DATA_DIR = project_root / "backend" / "data" / "processed"
            ACTIONS_PATH = DATA_DIR / "y_actions_weekly.csv"
            FUND_PATH = DATA_DIR / "Y_fund_weekly.csv"

            if not ACTIONS_PATH.exists() or not FUND_PATH.exists():
                return {
                    'error': "Data files not found",
                    'weights': pd.Series(),
                    'r2': 0,
                    'correlation': 0,
                    'tracking_error': 0,
                    'timeseries': pd.DataFrame()
                }

            actions = pd.read_csv(ACTIONS_PATH, parse_dates=["Date"])
            fund = pd.read_csv(FUND_PATH, parse_dates=["Date"])
            df = actions.merge(fund, on="Date", how="inner")

            action_cols = [c for c in df.columns if c not in ["Date", "Return"]]
            X = df[action_cols].values
            y = df["Return"].values

            def tracking_error_obj(weights, X, y):
                portfolio_returns = X @ weights
                return np.mean((y - portfolio_returns) ** 2)

            n_assets = len(action_cols)
            constraints = ({"type": "eq", "fun": lambda w: np.sum(w) - 1},)
            bounds = [(0, 1) for _ in range(n_assets)]
            w0 = np.ones(n_assets) / n_assets

            res = minimize(
                tracking_error_obj,
                w0,
                args=(X, y),
                method="SLSQP",
                bounds=bounds,
                constraints=constraints,
            )

            weights = pd.Series(res.x, index=action_cols).sort_values(ascending=False)

            df["Reconstructed_Return"] = X @ res.x
            df["Tracking_Error"] = df["Return"] - df["Reconstructed_Return"]

            te = np.sqrt(np.mean(df["Tracking_Error"] ** 2))
            corr = np.corrcoef(df["Return"], df["Reconstructed_Return"])[0, 1]

            from sklearn.metrics import r2_score
            r2 = r2_score(df["Return"], df["Reconstructed_Return"])

            timeseries = df[["Date", "Return", "Reconstructed_Return", "Tracking_Error"]].copy()
            timeseries.columns = ["Date", "WG_RETURN", "WG_REPL", "residual"]

            return {
                'weights': weights,
                'r2': r2,
                'correlation': corr,
                'tracking_error': te,
                'timeseries': timeseries
            }

        except Exception as e:
            return {
                'error': str(e),
                'weights': pd.Series(),
                'r2': 0,
                'correlation': 0,
                'tracking_error': 0,
                'timeseries': pd.DataFrame()
            }


class MLPredictor:
    """
    Wrapper pour les prédictions ML
    """

    @staticmethod
    def get_top_predictions(n_top=10):
        """
        Récupère les top N prédictions

        Returns:
            pd.DataFrame avec colonnes: Ticker, Predicted_Return, Factors
        """
        try:
            from pathlib import Path
            import os

            # Get project root (chemin absolu pour éviter les problèmes avec Streamlit)
            current_file = Path(__file__).resolve()
            project_root = current_file.parent.parent.parent.parent

            # Charger le dataset ML avec chemin absolu
            ML_DATASET = project_root / "backend" / "data" / "ml" / "action_ml_dataset.csv"

            if not ML_DATASET.exists():
                # Debug: montrer où on cherche
                print(f"DEBUG: Looking for ML dataset at: {ML_DATASET}")
                print(f"DEBUG: Project root: {project_root}")
                print(f"DEBUG: File exists: {ML_DATASET.exists()}")
                return pd.DataFrame()

            df = pd.read_csv(ML_DATASET, parse_dates=["Date"])

            # Get latest date
            latest_date = df["Date"].max()
            df_latest = df[df["Date"] == latest_date].copy()

            # Load model if exists (avec chemin absolu)
            MODEL_PATH = project_root / "backend" / "models" / "ridge_model.joblib"

            if MODEL_PATH.exists():
                from joblib import load
                model = load(MODEL_PATH)

                feature_cols = [
                    c for c in df.columns
                    if c not in ["Date", "Ticker", "Return_fwd", "Predicted_Return"]
                ]

                X = df_latest[feature_cols].values
                predictions = model.predict(X)

                df_latest["Predicted_Return"] = predictions
            else:
                # Fallback: use momentum as proxy
                df_latest["Predicted_Return"] = df_latest.get("Momentum_3M", 0)

            # Sort by predictions
            df_result = df_latest.nlargest(n_top, "Predicted_Return")

            return df_result[["Ticker", "Predicted_Return"] +
                           [c for c in df_latest.columns if c in ["Momentum_3M", "Volatility_3M", "Sharpe_3M"]]]

        except Exception as e:
            print(f"Error in get_top_predictions: {e}")
            return pd.DataFrame()

    @staticmethod
    def get_factor_analysis():
        """
        Analyse des facteurs pour toutes les actions
        """
        try:
            from pathlib import Path

            FEATURES_DIR = Path("backend/data/features")

            # Load latest momentum, volatility, sharpe
            momentum_files = list(FEATURES_DIR.glob("mom_*.csv"))
            vol_files = list(FEATURES_DIR.glob("vol_*.csv"))
            sharpe_files = list(FEATURES_DIR.glob("sharpe_*.csv"))

            if not (momentum_files and vol_files and sharpe_files):
                return pd.DataFrame()

            # Just return summary info
            return pd.DataFrame({
                'Factor': ['Momentum', 'Volatility', 'Sharpe'],
                'Available': ['Yes', 'Yes', 'Yes']
            })

        except Exception as e:
            print(f"Error in get_factor_analysis: {e}")
            return pd.DataFrame()
