"""
Construction de la target ML :
Rendement futur hebdomadaire (t+1)
à partir des rendements hebdomadaires existants
"""

import pandas as pd
from pathlib import Path

INPUT_FILE = Path("data/processed/X_actions_weekly_clean.csv")
OUTPUT_FILE = Path("data/processed/y_actions_weekly.csv")


def main():
    print("=" * 70)
    print("CONSTRUCTION DE y_ACTIONS_WEEKLY (TARGET ML)")
    print("=" * 70)

    # 1. Charger les rendements
    df = pd.read_csv(INPUT_FILE, parse_dates=["Date"])
    df = df.set_index("Date").sort_index()

    print(f"Données chargées : {df.shape[0]} dates | {df.shape[1]} actions")
    print(f"Période : {df.index.min().date()} → {df.index.max().date()}")

    # 2. Target = rendement futur (t+1)
    y = df.shift(-1)

    # 3. Supprimer la dernière date (pas de futur)
    y = y.iloc[:-1]

    # 4. Sauvegarde
    y.reset_index().to_csv(OUTPUT_FILE, index=False)

    print(f"\nTarget créée : {OUTPUT_FILE}")
    print(f"Dates valides : {y.shape[0]}")

    print("=" * 70)
    print("ETAPE 1 TERMINEE")
    print("=" * 70)


if __name__ == "__main__":
    main()
