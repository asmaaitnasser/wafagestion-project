# src/features/compute_sharpe.py

import pandas as pd
import numpy as np
from pathlib import Path

DATA_PATH = Path("data")
INPUT_FILE = DATA_PATH / "processed" / "X_actions_weekly_clean.csv"
OUTPUT_PATH = DATA_PATH / "features"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def compute_sharpe(prices: pd.DataFrame, window: int) -> pd.DataFrame:
    """
    Sharpe ratio hebdomadaire rolling + ranking cross-sectionnel
    """
    returns = prices.pct_change()

    mean_ret = returns.rolling(window).mean()
    vol = returns.rolling(window).std()

    sharpe = mean_ret / vol

    # Ranking cross-sectionnel (par date)
    sharpe_rank = sharpe.rank(axis=1, pct=True)

    return sharpe_rank


def main():
    print("=" * 70)
    print("CALCUL DU SHARPE RATIO (RANKING)")
    print("=" * 70)

    df = pd.read_csv(INPUT_FILE, parse_dates=["Date"])
    df = df.set_index("Date").sort_index()

    print(f"Données chargées : {df.shape[0]} dates | {df.shape[1]} actions")
    print(f"Période : {df.index.min().date()} → {df.index.max().date()}")

    windows = {
        "3m": 13,
        "6m": 26,
        "12m": 52
    }

    for label, window in windows.items():
        print(f"\nCalcul Sharpe {label.upper()} ({window} semaines)")
        sharpe = compute_sharpe(df, window)

        out_file = OUTPUT_PATH / f"sharpe_{label}.csv"
        sharpe.to_csv(out_file)

        valid_dates = sharpe.dropna(how="all").shape[0]
        print(f"  Sauvegardé : {out_file}")
        print(f"  Dates valides : {valid_dates}")


if __name__ == "__main__":
    main()
