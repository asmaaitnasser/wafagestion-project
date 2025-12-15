import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
import os

# =====================================================
# PARAMÈTRES
# =====================================================
WINDOW = 52          # 52 semaines (1 an)
ALPHA = 10.0

X_PATH = "data/processed/X_actions_weekly_clean.csv"
Y_PATH = "data/processed/Y_fund_weekly.csv"

OUT_WEIGHTS = "results/wg_actions_weights_rolling.csv"
OUT_TRACKING = "results/wg_actions_tracking_rolling.csv"

os.makedirs("results", exist_ok=True)

# =====================================================
# LOAD DATA
# =====================================================
X = pd.read_csv(X_PATH, parse_dates=["Date"])
Y = pd.read_csv(Y_PATH, parse_dates=["Date"])

X = X.set_index("Date")
Y = Y.set_index("Date")

# alignement strict
dates = X.index.intersection(Y.index)
X = X.loc[dates]
Y = Y.loc[dates]

tickers = X.columns.tolist()

print("======================================================================")
print("A1.3 — RECONSTITUTION DYNAMIQUE (ROLLING 52 SEMAINES)")
print("======================================================================")
print(f"Dates        : {dates.min().date()} → {dates.max().date()}")
print(f"Nb actions   : {len(tickers)}")
print()

# =====================================================
# ROLLING RECONSTRUCTION
# =====================================================
weights_records = []
tracking_records = []

for i in range(WINDOW, len(X)):
    date = X.index[i]

    X_window = X.iloc[i-WINDOW:i].values
    y_window = Y.iloc[i-WINDOW:i]["Return"].values

    model = Ridge(alpha=ALPHA, fit_intercept=False)
    model.fit(X_window, y_window)

    w = model.coef_

    # normalisation → somme des poids = 1
    if np.abs(w.sum()) > 1e-8:
        w = w / w.sum()

    # sauvegarde poids
    for ticker, weight in zip(tickers, w):
        weights_records.append({
            "Date": date,
            "Ticker": ticker,
            "Weight": weight
        })

    # reconstruction rendement
    r_real = Y.loc[date, "Return"]
    r_recon = np.dot(w, X.loc[date].values)

    tracking_records.append({
        "Date": date,
        "Return": r_real,
        "Reconstructed_Return": r_recon,
        "Tracking_Error": r_real - r_recon
    })

# =====================================================
# SAVE
# =====================================================
df_weights = pd.DataFrame(weights_records)
df_tracking = pd.DataFrame(tracking_records)

df_weights.to_csv(OUT_WEIGHTS, index=False)
df_tracking.to_csv(OUT_TRACKING, index=False)

rmse = np.sqrt(np.mean(df_tracking["Tracking_Error"] ** 2))
corr = df_tracking["Return"].corr(df_tracking["Reconstructed_Return"])

print("Pondérations sauvegardées :", OUT_WEIGHTS)
print("Tracking sauvegardé       :", OUT_TRACKING)
print()
print("QUALITÉ DE RECONSTRUCTION")
print(f"Tracking Error (RMSE) : {rmse:.4%}")
print(f"Corrélation          : {corr:.4f}")
