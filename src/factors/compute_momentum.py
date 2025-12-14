"""
Calcul du MOMENTUM (3M / 6M / 12M)
à partir des rendements hebdomadaires des actions
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ===============================
# PARAMÈTRES
# ===============================

INPUT_FILE = Path("data/processed/X_actions_weekly_clean.csv")
OUTPUT_DIR = Path("data/features")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WINDOWS = {
    "mom_3m": 13,   # ~ 3 mois
    "mom_6m": 26,   # ~ 6 mois
    "mom_12m": 52   # ~ 12 mois
}

# ===============================
# FONCTIONS
# ===============================

def load_returns(filepath: Path) -> pd.DataFrame:
    """Charge les rendements hebdomadaires"""
    df = pd.read_csv(filepath)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date").sort_index()
    return df


def compute_momentum(returns: pd.DataFrame, window: int) -> pd.DataFrame:
    """
    Momentum = produit cumulatif des (1 + r) - 1
    """
    momentum = (1 + returns).rolling(window=window).apply(
        np.prod, raw=True
    ) - 1
    return momentum


# ===============================
# MAIN
# ===============================

def main():
    print("=" * 70)
    print("CALCUL DU MOMENTUM")
    print("=" * 70)

    # 1. Charger les rendements
    returns = load_returns(INPUT_FILE)

    print(f"Données chargées : {returns.shape[0]} dates | {returns.shape[1]} actions")
    print(f"Période : {returns.index.min().date()} → {returns.index.max().date()}")

    # 2. Calculer chaque momentum
    for name, window in WINDOWS.items():
        print(f"\n→ Calcul {name.upper()} ({window} semaines)")

        mom = compute_momentum(returns, window)

        output_file = OUTPUT_DIR / f"{name}.csv"
        mom.to_csv(output_file)

        print(f"Sauvegardé : {output_file}")
        print(f"  Dates valides : {mom.dropna().shape[0]}")

    print("\n" + "=" * 70)
    print("MOMENTUM TERMINÉ")
    print("=" * 70)


if __name__ == "__main__":
    main()
