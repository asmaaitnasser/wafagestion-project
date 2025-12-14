import pandas as pd
from pathlib import Path

# ==========================================================
# CONFIG
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

ACTIONS_DIR = PROJECT_ROOT / "data" / "intermediate"
Y_FILE = PROJECT_ROOT / "data" / "processed" / "Y_fund_weekly.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "X_actions_weekly.csv"

# ==========================================================
# FONCTIONS UTILITAIRES
# ==========================================================

def detect_date_column(df):
    """
    Détecte automatiquement la colonne date
    """
    for col in df.columns:
        c = col.lower()
        if c in ["date", "séance", "seance", "date séance", "dateséance"]:
            return col
    raise ValueError("Colonne date introuvable dans le fichier")


def load_action_prices(file_path):
    """
    Charge un CSV d'action et retourne une série de prix Close
    """
    df = pd.read_csv(file_path)

    # --- détecter colonne Date ---
    date_col = detect_date_column(df)

    # --- détecter colonne Close ---
    close_candidates = ["close", "dernier cours", "dernier_cours", "cours"]
    close_col = None
    for col in df.columns:
        if col.lower() in close_candidates:
            close_col = col
            break

    if close_col is None:
        raise ValueError(f"Colonne Close introuvable dans {file_path.name}")

    # --- parsing ---
    df["Date"] = pd.to_datetime(df[date_col], dayfirst=True, errors="coerce")
    df["Close"] = pd.to_numeric(df[close_col], errors="coerce")

    df = df.dropna(subset=["Date", "Close"])
    df = df.sort_values("Date")

    return df.set_index("Date")["Close"]


def compute_weekly_returns(prices, ref_dates):
    """
    Calcule les rendements hebdomadaires alignés sur ref_dates
    """
    returns = []

    for d in ref_dates:
        # prix courant
        p_t = prices.loc[:d]
        if p_t.empty:
            returns.append(None)
            continue
        p_t = p_t.iloc[-1]

        # prix semaine précédente
        p_tm1 = prices.loc[:d - pd.Timedelta(days=7)]
        if p_tm1.empty:
            returns.append(None)
            continue
        p_tm1 = p_tm1.iloc[-1]

        returns.append((p_t / p_tm1) - 1)

    return returns

# ==========================================================
# PIPELINE PRINCIPAL
# ==========================================================

def main():
    print("=" * 70)
    print("CONSTRUCTION DE X_ACTIONS_WEEKLY")
    print("=" * 70)

    # 1) Charger Y (dates de référence)
    y = pd.read_csv(Y_FILE, parse_dates=["Date"])
    ref_dates = y["Date"].sort_values().tolist()

    print(f"✔ {len(ref_dates)} dates hebdomadaires chargées (WG ACTIONS)")

    # 2) Boucle sur les actions
    X = pd.DataFrame(index=ref_dates)

    action_files = sorted(ACTIONS_DIR.glob("*.csv"))
    print(f"✔ {len(action_files)} actions détectées")

    for file in action_files:
        ticker = file.stem
        try:
            prices = load_action_prices(file)
            weekly_returns = compute_weekly_returns(prices, ref_dates)
            X[ticker] = weekly_returns
            print(f"  [OK] {ticker}")
        except Exception as e:
            print(f"  [ERREUR] {ticker} -> {e}")

    # 3) Nettoyage final
    X.index.name = "Date"
    X = X.sort_index()
    X = X.dropna(axis=1, how="all")
    X = X.dropna()

    # 4) Sauvegarde
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    X.to_csv(OUTPUT_FILE)

    print("\n X_actions_weekly.csv généré")
    print(f" {OUTPUT_FILE}")
    print(f"Shape finale : {X.shape[0]} semaines x {X.shape[1]} actions")
    print("\nAperçu :")
    print(X.head())


if __name__ == "__main__":
    main()
