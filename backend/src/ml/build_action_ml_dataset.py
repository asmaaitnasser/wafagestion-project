"""
Construction du dataset ML niveau ACTION
"""

import pandas as pd
from pathlib import Path

FEATURES_DIR = Path("data/features")
OUTPUT_FILE = Path("data/ml/action_ml_dataset.csv")

FACTOR_FILES = [
    "mom_3m.csv",
    "mom_6m.csv",
    "mom_12m.csv",
    "vol_3m.csv",
    "vol_6m.csv",
    "vol_12m.csv",
    "sharpe_3m.csv",
    "sharpe_6m.csv",
    "sharpe_12m.csv",
]

RETURNS_FILE = Path("data/processed/y_actions_weekly.csv")


def main():
    print("=" * 70)
    print("CONSTRUCTION DATASET ML – ACTIONS")
    print("=" * 70)

    # 1. Charger les rendements actions
    y = pd.read_csv(RETURNS_FILE, parse_dates=["Date"])
    y = y.set_index("Date")

    # 2. Charger les facteurs
    factors = []

    for file in FACTOR_FILES:
        name = file.replace(".csv", "")
        df = pd.read_csv(FEATURES_DIR / file, parse_dates=["Date"])
        df = df.set_index("Date")

        df = df.stack().reset_index()
        df.columns = ["Date", "Ticker", name]
        factors.append(df)

    X = factors[0]
    for f in factors[1:]:
        X = X.merge(f, on=["Date", "Ticker"], how="inner")

    # 3. Ajouter la target (rendement futur)
    y_long = y.stack().reset_index()
    y_long.columns = ["Date", "Ticker", "Return"]

    y_long["Return_fwd"] = y_long.groupby("Ticker")["Return"].shift(-1)

    dataset = X.merge(
        y_long[["Date", "Ticker", "Return_fwd"]],
        on=["Date", "Ticker"],
        how="inner"
    )

    dataset = dataset.dropna().reset_index(drop=True)

    dataset.to_csv(OUTPUT_FILE, index=False)

    print(f" Dataset ML actions sauvegardé : {OUTPUT_FILE}")
    print(f"Lignes : {len(dataset)}")
    print(f"Actions : {dataset['Ticker'].nunique()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
