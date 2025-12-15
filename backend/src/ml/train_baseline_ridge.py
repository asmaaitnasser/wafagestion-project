"""
Baseline ML : Ridge Regression
Prédiction des rendements futurs des actions
"""

import pandas as pd
import numpy as np
from pathlib import Path
import os
from joblib import dump

from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_squared_error

DATASET = Path("data/ml/action_ml_dataset.csv")


def main():
    print("=" * 70)
    print("ENTRAINEMENT MODELE BASELINE – RIDGE")
    print("=" * 70)

    # 1. Charger les données
    df = pd.read_csv(DATASET, parse_dates=["Date"])

    # 2. Split temporel (IMPORTANT)
   # split_date = df["Date"].quantile(0.8)
    split_date = "2025-01-01"

    train = df[df["Date"] <= split_date]
    test = df[df["Date"] > split_date]

    print(f"Train: {train['Date'].min().date()} → {train['Date'].max().date()}")
    print(f"Test : {test['Date'].min().date()} → {test['Date'].max().date()}")

    # 3. Séparer X / y
    feature_cols = [
        c for c in df.columns
        if c not in ["Date", "Ticker", "Return_fwd"]
    ]

    X_train = train[feature_cols]
    y_train = train["Return_fwd"]

    X_test = test[feature_cols]
    y_test = test["Return_fwd"]

    # 4. Pipeline (scaling + ridge)
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("ridge", Ridge(alpha=1.0))
    ])

    # 5. Entraîner
    model.fit(X_train, y_train)

    # 6. Prédictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # 7. Évaluation
    print("\nRESULTATS")
    print("-" * 50)
    print(f"Train R² : {r2_score(y_train, y_pred_train):.4f}")
    print(f"Test  R² : {r2_score(y_test, y_pred_test):.4f}")
    print(f"Test  RMSE : {np.sqrt(mean_squared_error(y_test, y_pred_test)):.6f}")

    # 8. Importance des facteurs
    coefs = model.named_steps["ridge"].coef_
    importance = pd.Series(coefs, index=feature_cols).sort_values()

    print("\nIMPORTANCE DES FACTEURS")
    print("-" * 50)
    print(importance)

    # Sauvegarde
    importance.to_csv("data/ml/ridge_factor_importance.csv")
    print("\nImportances sauvegardées")

    # =========================
# SAUVEGARDE DU MODELE
# =========================
    os.makedirs("models", exist_ok=True)

    dump(model, "models/ridge_model.joblib")

    print("\nModèle sauvegardé dans models/ridge_model.joblib")



if __name__ == "__main__":
    main()
