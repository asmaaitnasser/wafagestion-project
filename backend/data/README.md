# Data Directory

Ce dossier contient les données du projet. Les fichiers volumineux ne sont pas versionnés sur GitHub.

## Structure

```
data/
├── raw/              # Données brutes téléchargées (ignorées par Git)
├── intermediate/     # Fichiers CSV intermédiaires (ignorés par Git)
├── features/         # Features calculées (ignorées par Git)
├── processed/        # Données nettoyées et prêtes à l'usage
└── ml/              # Datasets pour machine learning
```

## Comment Régénérer les Données

### 1. Télécharger les données ASFiM

```bash
cd ../..  # Retour à la racine du projet
python backend/src/scraping/scraping_asfim.py
```

Cela va créer le fichier `performance_hebdomadaire_asfim.xlsx` (22 MB).

### 2. Préparer les données

```bash
# Preprocessing
python backend/src/preprocessing/prepare_fund_timeseries.py
python backend/src/preprocessing/build_X_actions_weekly.py
python backend/src/preprocessing/build_y_actions_weekly.py
python backend/src/preprocessing/clean_X_actions_weekly.py

# Calculer les features
python backend/src/factors/compute_momentum.py
python backend/src/factors/compute_volatility.py
python backend/src/factors/compute_sharpe.py
```

### 3. Créer les datasets

```bash
# Dataset reconstruction
python backend/src/reconstruction/build_reconstruction_dataset.py

# Dataset ML
python backend/src/ml/build_action_ml_dataset.py
```

## Fichiers Importants Versionnés

- `processed/y_actions_weekly.csv` - Rendements hebdomadaires des actions
- `processed/Y_fund_weekly.csv` - Rendements du fonds WG Actions
- `ml/action_ml_dataset.csv` - Dataset pour entraînement ML

## Notes

- Les fichiers volumineux (>5MB) sont exclus du versioning Git
- Tous les fichiers peuvent être régénérés en exécutant les scripts ci-dessus
- Pour le développement, contactez le propriétaire du projet pour obtenir les données
