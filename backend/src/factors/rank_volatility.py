import pandas as pd
from pathlib import Path

FEATURES = ["vol_3m", "vol_6m", "vol_12m"]
INDIR = Path("data/features")

def rank_volatility(df):
    # Vol faible = bon score
    return df.rank(axis=1, ascending=True, pct=True)

def main():
    for f in FEATURES:
        print(f"\nRanking {f.upper()}")

        df = pd.read_csv(INDIR / f"{f}.csv", index_col=0, parse_dates=True)
        rank = rank_volatility(df)

        rank.to_csv(INDIR / f"{f}_rank.csv")
        print(f"  Sauvegardé : data/features/{f}_rank.csv")

if __name__ == "__main__":
    print("=" * 70)
    print("RANKING DES VOLATILITÉS")
    print("=" * 70)
    main()
