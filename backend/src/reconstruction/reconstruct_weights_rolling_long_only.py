import pandas as pd
import numpy as np
from scipy.optimize import minimize
from pathlib import Path

print("=" * 70)
print("A1.4.1 — RECONSTRUCTION ROLLING LONG-ONLY (13 SEMAINES)")
print("=" * 70)

# =====================
# PATHS
# =====================
DATA_ACTIONS = "data/processed/y_actions_weekly.csv"
DATA_FUND = "data/processed/Y_fund_weekly.csv"
OUT_WEIGHTS = "reconstruction/wg_actions_weights_rolling_long_only.csv"
OUT_TRACKING = "reconstruction/wg_actions_tracking_rolling_long_only.csv"

WINDOW = 13

Path("reconstruction").mkdir(exist_ok=True)

# =====================
# LOAD DATA
# =====================
X_all = pd.read_csv(DATA_ACTIONS, parse_dates=["Date"]).set_index("Date")
y_all = pd.read_csv(DATA_FUND, parse_dates=["Date"]).set_index("Date")["Return"]

# Align dates
dates = X_all.index.intersection(y_all.index)
X_all = X_all.loc[dates]
y_all = y_all.loc[dates]

tickers = X_all.columns

# =====================
# OPTIMISATION LONG ONLY
# =====================
def solve_long_only(X, y):
    n = X.shape[1]

    def objective(w):
        return np.mean((X @ w - y) ** 2)

    constraints = [
        {"type": "eq", "fun": lambda w: np.sum(w) - 1}
    ]

    bounds = [(0, 1) for _ in range(n)]
    w0 = np.ones(n) / n

    res = minimize(objective, w0, bounds=bounds, constraints=constraints)

    return res.x if res.success else None

# =====================
# ROLLING LOOP
# =====================
weights_records = []
tracking_records = []

for i in range(WINDOW, len(X_all)):
    date = X_all.index[i]

    X_win = X_all.iloc[i - WINDOW:i]
    y_win = y_all.iloc[i - WINDOW:i]

    w = solve_long_only(X_win.values, y_win.values)
    if w is None:
        continue

    # Save weights
    for t, wt in zip(tickers, w):
        weights_records.append({
            "Date": date,
            "Ticker": t,
            "Weight": wt
        })

    # Tracking
    real_ret = y_all.iloc[i]
    recon_ret = X_all.iloc[i] @ w

    tracking_records.append({
        "Date": date,
        "Return": real_ret,
        "Reconstructed_Return": recon_ret,
        "Tracking_Error": real_ret - recon_ret
    })

# =====================
# SAVE RESULTS
# =====================
pd.DataFrame(weights_records).to_csv(OUT_WEIGHTS, index=False)
pd.DataFrame(tracking_records).to_csv(OUT_TRACKING, index=False)

print(" Poids sauvegardés :", OUT_WEIGHTS)
print("Tracking sauvegardé :", OUT_TRACKING)
