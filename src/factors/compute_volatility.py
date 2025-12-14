import pandas as pd
import numpy as np
from pathlib import Path

INPUT = "data/processed/X_actions_weekly_clean.csv"
OUTDIR = Path("data/features")
OUTDIR.mkdir(parents=True, exist_ok=True)

WINDOWS = {
    "vol_3m": 13,
    "vol_6m": 26,
    "vol_12m": 52
}

def main():
    df = pd.read_csv(INPUT, index_col=0, parse_dates=True)

    print(f"Données chargées : {df.shape[0]} dates | {df.shape[1]} actions")
    print(f"Période : {df.index.min().date()} → {df.index.max().date()}")

    for name, window in WINDOWS.items():
        print(f"\nCalcul {name.upper()} ({window} semaines)")

        vol = df.rolling(window).std() * np.sqrt(52)
        vol.to_csv(OUTDIR / f"{name}.csv")

        print(f"  Sauvegardé : data/features/{name}.csv")
        print(f"  Dates valides : {vol.dropna().shape[0]}")

if __name__ == "__main__":
    print("=" * 70)
    print("CALCUL DES VOLATILITÉS")
    print("=" * 70)
    main()
