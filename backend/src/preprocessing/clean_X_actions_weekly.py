import pandas as pd

# Charger les rendements
df = pd.read_csv("data/processed/X_actions_weekly.csv")

# Date
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").drop_duplicates(subset="Date")

# Colonnes actions
action_cols = df.columns.drop("Date")
df[action_cols] = df[action_cols].apply(pd.to_numeric, errors="coerce")

# Sauvegarde cleaned-light
df.to_csv("data/processed/X_actions_weekly_clean.csv", index=False)

print(" Nettoyage léger terminé")
print(f"Période : {df['Date'].min().date()} → {df['Date'].max().date()}")
print(f"Actions : {len(action_cols)}")
