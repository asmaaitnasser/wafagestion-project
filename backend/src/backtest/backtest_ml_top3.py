import pandas as pd
import numpy as np
from joblib import load

print("=" * 70)
print("BACKTEST PORTEFEUILLE ML – TOP 3 ACTIONS / SEMAINE")
print("=" * 70)

# ======================
# 1. Chargement données
# ======================
df = pd.read_csv(
    "data/ml/action_ml_dataset.csv",
    parse_dates=["Date"]
)

model = load("models/ridge_model.joblib")

features = [
    "mom_3m", "mom_6m", "mom_12m",
    "vol_3m", "vol_6m", "vol_12m",
    "sharpe_3m", "sharpe_6m", "sharpe_12m"
]

# ======================
# 2. Prédictions ML
# ======================
df["pred_return"] = model.predict(df[features])

# ======================
# 3. Construction portefeuille
# ======================
portfolio_returns = []

for date, group in df.groupby("Date"):

    # Top 3 actions selon le score ML
    top3 = group.sort_values("pred_return", ascending=False).head(3)

    # Rendement réalisé (t+1)
    realized_return = top3["Return_fwd"].mean()

    portfolio_returns.append({
        "Date": date,
        "portfolio_return": realized_return
    })

portfolio = pd.DataFrame(portfolio_returns).sort_values("Date")

# ======================
# 4. Performance cumulée
# ======================
portfolio["cum_return"] = (1 + portfolio["portfolio_return"]).cumprod()

# ======================
# 5. Sauvegarde
# ======================
portfolio.to_csv(
    "results/portfolio_ml_top3_weekly.csv",
    index=False
)

print("Backtest terminé.")
print(f"Période : {portfolio['Date'].min().date()} → {portfolio['Date'].max().date()}")
print(f"Rendement total : {portfolio['cum_return'].iloc[-1] - 1:.2%}")
