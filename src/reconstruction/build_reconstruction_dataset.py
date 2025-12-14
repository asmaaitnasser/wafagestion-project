# -*- coding: utf-8 -*-
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUT_DIR = Path("datasets")
OUT_DIR.mkdir(parents=True, exist_ok=True)

ACTIONS_PATH = DATA_DIR / "processed" / "y_actions_weekly.csv"
FUND_PATH    = DATA_DIR / "processed" / "Y_fund_weekly.csv"

OUT_PATH = OUT_DIR / "wg_actions_reconstruction_dataset.csv"


def main():
    fund = pd.read_csv(FUND_PATH, parse_dates=["Date"])
    actions = pd.read_csv(ACTIONS_PATH, parse_dates=["Date"])

    fund = fund.rename(columns={"Return": "WG_RETURN"}).sort_values("Date")
    actions = actions.sort_values("Date")

    # Inner join: on garde uniquement les semaines communes
    df = pd.merge(actions, fund[["Date", "WG_RETURN"]], on="Date", how="inner")

    # Nettoyage
    df = df.drop_duplicates(subset=["Date"]).sort_values("Date")

    # Convertir toutes les colonnes actions en numeric
    action_cols = [c for c in df.columns if c not in ["Date", "WG_RETURN"]]
    for c in action_cols + ["WG_RETURN"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Drop rows avec NaN (tu peux aussi faire ffill si besoin, mais pour reconstitution c'est mieux d'être strict)
    before = len(df)
    df = df.dropna(subset=action_cols + ["WG_RETURN"])
    after = len(df)

    print("==============================================================")
    print("DATASET RECONSTITUTION WG ACTIONS")
    print("==============================================================")
    print(f"Dates : {df['Date'].min().date()} → {df['Date'].max().date()}")
    print(f"Lignes: {before} → {after} après dropna")
    print(f"Nb actions (features): {len(action_cols)}")
    print("Actions:", ", ".join(action_cols))

    df.to_csv(OUT_PATH, index=False)
    print(f"\nDataset sauvegardé: {OUT_PATH}")


if __name__ == "__main__":
    main()
