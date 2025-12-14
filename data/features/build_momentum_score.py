"""
Construction du score momentum global
Combinaison des rankings momentum 3M, 6M et 12M
"""

import pandas as pd
from pathlib import Path

# ===============================
# PARAMÈTRES
# ===============================
DATA_DIR = Path("data/features")

FILE_MOM_3M = DATA_DIR / "mom_3m_rank.csv"
FILE_MOM_6M = DATA_DIR / "mom_6m_rank.csv"
FILE_MOM_12M = DATA_DIR / "mom_12m_rank.csv"

OUTPUT_FILE = DATA_DIR / "momentum_score.csv"

# Pondérations (standard académique)
W_3M = 0.2
W_6M = 0.3
W_12M = 0.5


# ===============================
# FONCTIONS
# ===============================
def load_rank(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    df = df.sort_index()
    return df


def main():
    print("=" * 70)
    print("CONSTRUCTION DU SCORE MOMENTUM GLOBAL")
    print("=" * 70)

    # 1️ Charger les rankings
    mom_3m = load_rank(FILE_MOM_3M)
    mom_6m = load_rank(FILE_MOM_6M)
    mom_12m = load_rank(FILE_MOM_12M)

    print(f" MOM 3M  : {mom_3m.shape}")
    print(f" MOM 6M  : {mom_6m.shape}")
    print(f" MOM 12M : {mom_12m.shape}")

    # 2️ Aligner les dates communes
    common_dates = mom_3m.index \
        .intersection(mom_6m.index) \
        .intersection(mom_12m.index)

    mom_3m = mom_3m.loc[common_dates]
    mom_6m = mom_6m.loc[common_dates]
    mom_12m = mom_12m.loc[common_dates]

    print(f"Dates communes : {len(common_dates)}")

    # 3️ Calcul du score momentum global
    momentum_score = (
        W_12M * mom_12m +
        W_6M * mom_6m +
        W_3M * mom_3m
    )

    # 4️ Nettoyage
    momentum_score = momentum_score.sort_index()

    # 5️ Sauvegarde
    momentum_score.to_csv(OUTPUT_FILE)

    print(f"\n Score momentum sauvegardé : {OUTPUT_FILE}")
    print(f" Période : {momentum_score.index.min().date()} → {momentum_score.index.max().date()}")
    print(f" Actions : {len(momentum_score.columns)}")

    print("\n" + "=" * 70)
    print("SCORE MOMENTUM GLOBAL TERMINÉ")
    print("=" * 70)


if __name__ == "__main__":
    main()
