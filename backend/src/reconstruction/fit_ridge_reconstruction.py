# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pathlib import Path

from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

DATASET_PATH = Path("datasets/wg_actions_reconstruction_dataset.csv")
OUT_DIR = Path("results/reconstruction")
OUT_DIR.mkdir(parents=True, exist_ok=True)

WEIGHTS_PATH = OUT_DIR / "wg_actions_weights_ridge.csv"
ERRORS_PATH = OUT_DIR / "wg_actions_tracking_error_timeseries.csv"
SUMMARY_PATH = OUT_DIR / "wg_actions_summary.txt"


def main():
    df = pd.read_csv(DATASET_PATH, parse_dates=["Date"]).sort_values("Date")

    y = df["WG_RETURN"].values
    feature_cols = [c for c in df.columns if c not in ["Date", "WG_RETURN"]]
    X = df[feature_cols].values

    # Pipeline : standardiser puis Ridge
    # Important: ici on estime une "réplication", pas une prédiction.
    model = Pipeline([
        ("scaler", StandardScaler(with_mean=True, with_std=True)),
        ("ridge", Ridge(alpha=1.0, fit_intercept=True))
    ])

    model.fit(X, y)
    y_hat = model.predict(X)

    # Metrics reconstitution
    r2 = r2_score(y, y_hat)
    resid = y - y_hat
    tracking_error = np.std(resid, ddof=1)  # TE hebdo
    corr = np.corrcoef(y, y_hat)[0, 1]

    # Poids sur échelle standardisée => pour interprétation "poids", c'est mieux d'afficher contribution via coefficients * sigma.
    # On sort quand même les coefficients, puis on les convertit en "poids relatifs" positifs si tu veux.
    ridge = model.named_steps["ridge"]
    coef = ridge.coef_
    intercept = ridge.intercept_

    weights = pd.Series(coef, index=feature_cols).sort_values(ascending=False)

    # Sauvegardes
    weights.to_csv(WEIGHTS_PATH, header=["ridge_coef"])
    pd.DataFrame({
        "Date": df["Date"],
        "WG_RETURN": y,
        "WG_REPL": y_hat,
        "residual": resid
    }).to_csv(ERRORS_PATH, index=False)

    summary = []
    summary.append("==============================================================")
    summary.append("RECONSTITUTION WG ACTIONS — RIDGE (FULL SAMPLE)")
    summary.append("==============================================================")
    summary.append(f"Période : {df['Date'].min().date()} → {df['Date'].max().date()}")
    summary.append(f"Nb obs  : {len(df)}")
    summary.append(f"Nb actions/features : {len(feature_cols)}")
    summary.append("")
    summary.append("METRICS (reconstitution)")
    summary.append(f"R²            : {r2:.4f}")
    summary.append(f"Corr(y, yhat) : {corr:.4f}")
    summary.append(f"Tracking Error (hebdo, std resid) : {tracking_error:.6f}")
    summary.append("")
    summary.append(f"Intercept (hebdo): {intercept:.6f}")
    summary.append("")
    summary.append("TOP 10 COEFS (pas encore des pondérations OPCVM, juste signal linéaire)")
    for k, v in weights.head(10).items():
        summary.append(f"{k:6s}  {v:+.6f}")

    txt = "\n".join(summary)
    print(txt)
    SUMMARY_PATH.write_text(txt, encoding="utf-8")

    print(f"\nCoefs sauvegardés: {WEIGHTS_PATH}")
    print(f"Série erreur sauvegardée: {ERRORS_PATH}")
    print(f"Summary sauvegardé: {SUMMARY_PATH}")

    # Option utile: afficher top 10 contributions en valeur absolue
    print("\nTOP 10 |coef|")
    print(weights.abs().sort_values(ascending=False).head(10))


if __name__ == "__main__":
    main()
