import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/features")

FILES = {
    "3m": DATA_PATH / "sharpe_3m.csv",
    "6m": DATA_PATH / "sharpe_6m.csv",
    "12m": DATA_PATH / "sharpe_12m.csv"
}

WEIGHTS = {
    "3m": 0.3,
    "6m": 0.3,
    "12m": 0.4
}

OUTPUT_FILE = DATA_PATH / "sharpe_score.csv"


def load_factor(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date"])
    return df.set_index("Date").sort_index()


def main():
    print("=" * 70)
    print("CONSTRUCTION DU SCORE SHARPE GLOBAL")
    print("=" * 70)

    sharpe_factors = {}
    for horizon, file in FILES.items():
        print(f"Chargement : {file.name}")
        sharpe_factors[horizon] = load_factor(file)

    # Alignement des dates
    common_index = sharpe_factors["3m"].index
    for df in sharpe_factors.values():
        common_index = common_index.intersection(df.index)

    # Score pondéré
    sharpe_score = sum(
        WEIGHTS[h] * sharpe_factors[h].loc[common_index]
        for h in WEIGHTS
    )

    sharpe_score = sharpe_score.sort_index()

    sharpe_score.to_csv(OUTPUT_FILE)
    print(f"\n✔ Score Sharpe sauvegardé : {OUTPUT_FILE}")

    print(f"Dates : {sharpe_score.index.min().date()} → {sharpe_score.index.max().date()}")
    print(f"Actions : {sharpe_score.shape[1]}")


if __name__ == "__main__":
    main()
