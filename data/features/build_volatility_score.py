import pandas as pd
from pathlib import Path

FEATURES_DIR = Path("data/features")

FILES = {
    "vol_3m": "vol_3m_rank.csv",
    "vol_6m": "vol_6m_rank.csv",
    "vol_12m": "vol_12m_rank.csv",
}

OUTPUT = FEATURES_DIR / "volatility_score.csv"

def main():
    print("Chargement des rankings de volatilité...")

    dfs = []
    for name, file in FILES.items():
        df = pd.read_csv(FEATURES_DIR / file, index_col=0, parse_dates=True)
        dfs.append(df)

    # Alignement parfait dates / actions
    vol_score = sum(dfs) / len(dfs)

    vol_score.to_csv(OUTPUT)

    print("Score de volatilité global calculé")
    print(f"Sauvegardé : {OUTPUT}")
    print(f"Période : {vol_score.index.min().date()} → {vol_score.index.max().date()}")
    print(f"Actions : {vol_score.shape[1]}")

if __name__ == "__main__":
    print("=" * 70)
    print("CALCUL DU SCORE DE VOLATILITÉ GLOBAL")
    print("=" * 70)
    main()
