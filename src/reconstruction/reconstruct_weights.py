# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.optimize import minimize

# ==============================
# PATHS
# ==============================
DATA_DIR = Path("data/processed")
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

ACTIONS_PATH = DATA_DIR / "y_actions_weekly.csv"
FUND_PATH = DATA_DIR / "Y_fund_weekly.csv"

OUT_WEIGHTS = RESULTS_DIR / "wg_actions_weights.csv"
OUT_TRACKING = RESULTS_DIR / "wg_actions_tracking.csv"


# ==============================
# OBJECTIVE FUNCTION
# ==============================
def tracking_error(weights, X, y):
    """
    Minimise la tracking error quadratique
    """
    portfolio_returns = X @ weights
    return np.mean((y - portfolio_returns) ** 2)


# ==============================
# MAIN
# ==============================
def main():
    print("=" * 70)
    print("A1.2 — RECONSTITUTION DU PORTEFEUILLE WG ACTIONS")
    print("=" * 70)

    # Load data
    actions = pd.read_csv(ACTIONS_PATH, parse_dates=["Date"])
    fund = pd.read_csv(FUND_PATH, parse_dates=["Date"])

    # Merge
    df = actions.merge(fund, on="Date", how="inner")

    action_cols = [c for c in df.columns if c not in ["Date", "Return"]]

    X = df[action_cols].values
    y = df["Return"].values

    print(f"Dates        : {df['Date'].min().date()} → {df['Date'].max().date()}")
    print(f"Nb actions   : {len(action_cols)}")

    # ==============================
    # CONSTRAINTS
    # ==============================
    n_assets = len(action_cols)

    constraints = (
        {"type": "eq", "fun": lambda w: np.sum(w) - 1},  # somme = 1
    )

    bounds = [(0, 1) for _ in range(n_assets)]  # w_i >= 0

    w0 = np.ones(n_assets) / n_assets  # initialisation neutre

    # ==============================
    # OPTIMISATION
    # ==============================
    res = minimize(
        tracking_error,
        w0,
        args=(X, y),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    weights = pd.Series(res.x, index=action_cols).sort_values(ascending=False)

    # ==============================
    # SAVE WEIGHTS
    # ==============================
    weights.to_csv(OUT_WEIGHTS)
    print(f"\nPondérations sauvegardées : {OUT_WEIGHTS}")

    # ==============================
    # TRACKING
    # ==============================
    df["Reconstructed_Return"] = X @ res.x
    df["Tracking_Error"] = df["Return"] - df["Reconstructed_Return"]

    df_out = df[["Date", "Return", "Reconstructed_Return", "Tracking_Error"]]
    df_out.to_csv(OUT_TRACKING, index=False)

    print(f"Tracking sauvegardé       : {OUT_TRACKING}")

    # ==============================
    # METRICS
    # ==============================
    te = np.sqrt(np.mean(df["Tracking_Error"] ** 2))
    corr = np.corrcoef(df["Return"], df["Reconstructed_Return"])[0, 1]

    print("\nQUALITÉ DE RECONSTRUCTION")
    print(f"Tracking Error (RMSE) : {te:.4%}")
    print(f"Corrélation          : {corr:.4f}")

    print("\nTop 5 pondérations :")
    print(weights.head())


if __name__ == "__main__":
    main()
