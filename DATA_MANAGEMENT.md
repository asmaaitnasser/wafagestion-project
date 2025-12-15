# 📁 Gestion des Données - Wafa Gestion Project

## ⚠️ Fichiers NON Versionnés sur GitHub

Pour éviter de dépasser les limites GitHub et garder le repo léger, les fichiers suivants sont exclus :

### 🚫 Fichiers Volumineux (>5MB)

| Fichier/Dossier | Taille | Raison | Comment Obtenir |
|-----------------|--------|--------|-----------------|
| `performance_hebdomadaire_asfim.xlsx` | 22 MB | Données brutes ASFiM | `python backend/src/scraping/scraping_asfim.py` |
| `backend/data/raw/` | Variable | Fichiers Excel téléchargés | Script scraping |
| `backend/data/intermediate/` | ~10 MB | CSV intermédiaires par action | Scripts preprocessing |
| `backend/data/features/` | ~5 MB | Features calculées | Scripts factors |

### 🔐 Fichiers Secrets (JAMAIS push)

- `.env`, `.env.local`, `.env.production` - Variables d'environnement
- `frontend/.streamlit/secrets.toml` - Secrets Streamlit (API keys, etc.)
- `credentials.json`, `*.pem`, `*.key` - Credentials et clés

### 🗑️ Fichiers Temporaires

- `__pycache__/`, `*.pyc` - Cache Python
- `.ipynb_checkpoints/` - Checkpoints Jupyter
- `venv/`, `env/` - Environnements virtuels
- `tmp/`, `temp/`, `test_output/` - Fichiers temporaires

### 📊 Résultats Générés (peuvent être régénérés)

- `backend/results/**/*.csv` - Résultats de reconstruction
- `backend/results/**/*.txt` - Rapports texte
- `backend/datasets/*.csv` - Datasets ML (sauf si <5MB)

## ✅ Fichiers VERSIONNÉS sur GitHub

### Code Source
- `backend/src/**/*.py` - Tout le code Python
- `frontend/**/*.py` - Code du dashboard
- `deployment/**` - Configuration déploiement

### Données Essentielles (si <5MB)
- `backend/data/processed/y_actions_weekly.csv` - Rendements actions
- `backend/data/processed/Y_fund_weekly.csv` - Rendements fonds
- `backend/data/ml/action_ml_dataset.csv` - Dataset ML

### Modèles ML (si <10MB)
- `backend/models/ridge_model.joblib` - Modèle Ridge entraîné (si <10MB)

### Configuration
- `requirements.txt` - Dépendances Python
- `.gitignore` - Exclusions Git
- `README.md` - Documentation
- `deployment/Dockerfile`, `render.yaml`, etc. - Config déploiement

### Présentation
- `presentation/slides.pptx` - Slides pour le jury
- `presentation/screenshots/*.png` - Captures d'écran
- **⚠️ NE PAS push `demo.mp4` si >50MB** → Uploader sur YouTube/Loom

## 🔄 Comment Régénérer les Données (pour un nouveau contributeur)

### 1️⃣ Cloner le Projet
```bash
git clone https://github.com/votre-username/wafagestion.git
cd wafagestion
```

### 2️⃣ Installer les Dépendances
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Scraper les Données ASFiM
```bash
python backend/src/scraping/scraping_asfim.py
# Génère: performance_hebdomadaire_asfim.xlsx (22 MB)
```

### 4️⃣ Préprocessing
```bash
python backend/src/preprocessing/prepare_fund_timeseries.py
python backend/src/preprocessing/build_X_actions_weekly.py
python backend/src/preprocessing/build_y_actions_weekly.py
python backend/src/preprocessing/clean_X_actions_weekly.py
```

### 5️⃣ Calculer les Features
```bash
python backend/src/factors/compute_momentum.py
python backend/src/factors/compute_volatility.py
python backend/src/factors/compute_sharpe.py
```

### 6️⃣ Créer les Datasets
```bash
python backend/src/reconstruction/build_reconstruction_dataset.py
python backend/src/ml/build_action_ml_dataset.py
```

### 7️⃣ Entraîner les Modèles
```bash
python backend/src/ml/train_baseline_ridge.py
python backend/src/reconstruction/fit_ridge_reconstruction.py
```

## 📦 Alternative : Télécharger les Données Préparées

Si vous ne voulez pas tout régénérer, demandez au propriétaire du projet un fichier ZIP contenant :
- `performance_hebdomadaire_asfim.xlsx`
- `backend/data/processed/`
- `backend/models/ridge_model.joblib`

## 🎯 Pour le Challenge Wafa Gestion

### Fichiers à Inclure dans le Dossier Google Drive

1. ✅ **Présentation PPT** - `presentation/slides.pptx`
2. ✅ **Lien déployé** - URL de votre app (Render/Streamlit Cloud)
3. ✅ **Screenshots/Vidéo** - `presentation/screenshots/` + `demo.mp4` (ou lien YouTube)
4. ✅ **CV** - Votre CV

### ⚠️ NE PAS Inclure
- ❌ Code source complet (il est sur GitHub)
- ❌ Fichiers de données volumineux (>50MB)
- ❌ Environnement virtuel

## 📝 Commandes Git Utiles

### Vérifier ce qui sera push
```bash
git status
git diff --cached
```

### Vérifier la taille du repo
```bash
git count-objects -vH
```

### Si vous avez accidentellement commité un gros fichier
```bash
# Supprimer du tracking mais garder localement
git rm --cached performance_hebdomadaire_asfim.xlsx
git commit -m "Remove large data file from tracking"

# Si déjà push, nettoyer l'historique (avancé)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch performance_hebdomadaire_asfim.xlsx" \
  --prune-empty --tag-name-filter cat -- --all
```

## 🔍 Vérifier Avant de Push

```bash
# Liste tous les fichiers trackés
git ls-files

# Chercher les gros fichiers
git ls-files | xargs ls -lh | sort -k5 -hr | head -20

# Tester le .gitignore
git status --ignored
```

## 🌐 Limites GitHub

- **Fichier unique** : Max 100 MB (erreur), warning à 50 MB
- **Repo total** : Recommandé <1 GB
- **Push** : Max 2 GB par push

Si vous devez stocker de gros fichiers, utilisez :
- **Git LFS** (Large File Storage)
- **Google Drive** pour partage temporaire
- **DVC** (Data Version Control) pour données ML
