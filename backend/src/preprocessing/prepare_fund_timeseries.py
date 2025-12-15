import pandas as pd
import re
from pathlib import Path

# ==========================================================
# CONFIG
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "performance_hebdomadaire_asfim.xlsx"
OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "Y_fund_weekly.csv"

WG_ISINS = ["MA0000040321", "MA0000042293"]
  # WG ACTIONS

# ==========================================================
# FONCTION UTILITAIRE
# ==========================================================

def extract_date(filename: str):
    """
    Extrait la date (DD-MM-YYYY) depuis le nom du fichier ASFiM
    """
    match = re.search(r"(\d{2}-\d{2}-\d{4})", filename)
    if match:
        return pd.to_datetime(match.group(1), format="%d-%m-%Y")
    return pd.NaT

# ==========================================================
# PIPELINE PRINCIPAL
# ==========================================================

def main():
    # 1) Vérifier l'existence du fichier source
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Fichier introuvable : {INPUT_FILE}")

    # 2) Créer le dossier de sortie si nécessaire
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # 3) Charger le fichier fusionné ASFiM
    df = pd.read_excel(INPUT_FILE)

    # 4) Extraire la date depuis source_file
    df["Date"] = df["source_file"].apply(extract_date)

    if df["Date"].isna().any():
        raise ValueError("Certaines dates n'ont pas pu être extraites depuis source_file")

    # 5) Filtrer WG ACTIONS
    df = df[df["CODE ISIN"].isin(WG_ISINS)].copy()

    if df.empty:
        raise ValueError("WG ACTIONS non trouvé (ISIN incorrect ?)")

    # 6) Trier par date (OBLIGATOIRE)
    df = df.sort_values("Date")

    # ======================================================
    # CORRECTION IMPORTANTE (TON PROBLÈME)
    # ======================================================
    # Supprimer les dates dupliquées (ex: 2023-03-17 en double)
    df = df.drop_duplicates(subset=["Date"])

    # Réinitialiser l'index (propreté)
    df = df.reset_index(drop=True)

    # ======================================================
    # 7) Construire la série de rendements hebdomadaires
    # ======================================================
    # On utilise directement la performance ASFiM "1 semaine"
    df["Return"] = df["1 semaine"]

    # 8) Dataset final
    df_final = df[["Date", "Return"]]

    # 9) Sauvegarde
    df_final.to_csv(OUTPUT_FILE, index=False)

    print(" Série temporelle WG ACTIONS prête")
    print(f" Fichier généré : {OUTPUT_FILE}")
    print(df_final.head())

# ==========================================================
# EXECUTION
# ==========================================================

if __name__ == "__main__":
    main()
