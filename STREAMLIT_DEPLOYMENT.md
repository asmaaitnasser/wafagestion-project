# Déploiement Streamlit Cloud

## Configuration

- **Main file path**: `frontend/app.py`
- **Python version**: 3.10
- **Branch**: main

## Fichiers Essentiels

Les fichiers suivants doivent être présents sur GitHub pour le déploiement:

### Code
- `frontend/app.py` - Application principale
- `frontend/pages/*.py` - Pages du dashboard
- `backend/src/**/*.py` - Code backend

### Données (fichiers légers)
- `backend/datasets/wg_actions_reconstruction_dataset.csv` (43 KB)
- `backend/data/ml/action_ml_dataset.csv` (433 KB)
- `backend/models/ridge_model.joblib` (1.8 KB)

### Configuration
- `requirements.txt` - Dépendances Python
- `.streamlit/config.toml` - Configuration Streamlit (thème Wafa Gestion)

## Vérification Avant Déploiement

```bash
# 1. Vérifier que l'app fonctionne localement
streamlit run frontend/app.py

# 2. Vérifier les fichiers trackés par git
git ls-files | grep -E "(datasets|models|data/ml)"

# 3. Vérifier la taille du repo
git count-objects -vH
```

## URL de Déploiement

Une fois déployé, l'application sera accessible sur:
`https://wafagestion-[votre-username].streamlit.app`
