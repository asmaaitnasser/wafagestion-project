"""
Ranking cross-sectionnel du momentum
Transforme les momentum bruts en scores relatifs [0, 1]
"""

import pandas as pd
from pathlib import Path

# ===============================
# PARAMÈTRES
# ===============================

FEATURES_DIR = Path("data/features")
OUTPUT_DIR = Path("data/features")
OUTPUT_DIR.mkdir(exist_ok=True)

MOM_FILES = {
    "mom_3m": FEATURES_DIR / "mom_3m.csv",
    "mom_6m": FEATURES_DIR / "mom_6m.csv",
    "mom_12m": FEATURES_DIR / "mom_12m.csv",
}

# ===============================
# FONCTIONS
# ===============================

def load_factor(filepath: Path) -> pd.DataFrame:
    """Charge un facteur avec Date en index"""
    df = pd.read_csv(filepath)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date").sort_index()
    return df


def rank_cross_section(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ranking cross-sectionnel par date
    Score ∈ [0, 1]
    """
    ranked = df.rank(axis=1, method="average", pct=True)
    return ranked


# ===============================
# MAIN
# ===============================

def main():
    print("=" * 70)
    print("RANKING DU MOMENTUM")
    print("=" * 70)

    for name, path in MOM_FILES.items():
        print(f"\nTraitement {name.upper()}")

        df = load_factor(path)
        ranked = rank_cross_section(df)

        output_file = OUTPUT_DIR / f"{name}_rank.csv"
        ranked.to_csv(output_file)

        print(f"Sauvegardé : {output_file}")
        print(f"  Dates valides : {ranked.dropna(how='all').shape[0]}")

    print("\n" + "=" * 70)
    print("RANKING TERMINÉ")
    print("=" * 70)


if __name__ == "__main__":
    main()
