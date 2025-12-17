# 🏦 Wafa Gestion - Portfolio Intelligence Platform

**Challenge Data & AI Internship 2026**

Plateforme d'analyse quantitative pour la reconstruction et l'optimisation de portefeuilles OPCVM.

---

## 🎯 Objectif du Projet

Reconstituer le portefeuille réel d'un OPCVM (WG Actions) en utilisant des techniques d'optimisation et de machine learning, permettant aux gérants de fonds et analystes de :

- ✅ Comprendre la composition des portefeuilles concurrents
- ✅ Identifier les opportunités d'investissement via ML
- ✅ Optimiser les allocations d'actifs
- ✅ Monitorer les risques et la performance

---

## 🚀 Fonctionnalités Principales

### 1. 🔄 Reconstruction de Portefeuille
- **Algorithmes** : Ridge Regression, SLSQP Optimization
- **Métriques** : Tracking Error, R², Corrélation
- **Visualisations** : Pondérations, Performance temporelle
- **Export** : CSV des pondérations et séries temporelles

### 2. 🔮 Prédictions ML
- **Modèle** : Ridge Regression avec facteurs techniques
- **Facteurs** : Momentum, Volatilité, Sharpe Ratio
- **Output** : Top actions recommandées
- **Backtesting** : Stratégies d'investissement

### 3. 📊 Analytics & Insights
- Analyse comparative multi-fonds
- Détection d'anomalies
- Rapports automatiques

---

## 📁 Structure du Projet

```
wafagestion/
│
├── backend/                          # Code Python (analyse quantitative)
│   ├── src/
│   │   ├── reconstruction/          # Algorithmes de reconstruction
│   │   ├── ml/                      # Machine Learning
│   │   ├── factors/                 # Calcul des facteurs techniques
│   │   ├── preprocessing/           # Nettoyage des données
│   │   ├── scraping/                # Scraping données ASFiM
│   │   └── api/                     # Wrapper pour frontend
│   ├── data/                        # Données (non versionnées)
│   ├── models/                      # Modèles ML entraînés
│   └── results/                     # Résultats (non versionnés)
│
├── frontend/                         # Application Web (Streamlit)
│   ├── app.py                       # Application principale
│   ├── pages/                       # Pages du dashboard
│   │   ├── reconstruction.py
│   │   └── predictions.py
│   └── .streamlit/                  # Configuration
│
├── presentation/                     # Pour le challenge
│   ├── screenshots/
│   ├── demo.mp4
│   └── slides.pptx
│
├── requirements.txt                  # Dépendances Python
├── DEPLOYMENT_GUIDE.md              # Guide de déploiement
└── DATA_MANAGEMENT.md               # Gestion des données

```

---

## ⚡ Démarrage Rapide

### 1. Cloner le Repository
```bash
git clone https://github.com/votre-username/wafagestion.git
cd wafagestion
```

### 2. Installer les Dépendances
```bash
pip install -r requirements.txt
```

### 3. Lancer l'Application Web
```bash
streamlit run frontend/app.py
```

L'application sera accessible sur : **http://localhost:8501**

---

## 📊 Données

Les données proviennent de l'**ASFiM** (Association des Sociétés de Gestion et Fonds d'Investissement Marocains).

Les fichiers volumineux ne sont pas versionnés sur GitHub. Pour régénérer les données :

```bash
# Scraper les données ASFiM
python backend/src/scraping/scraping_asfim.py

# Préprocessing
python backend/src/preprocessing/prepare_fund_timeseries.py
python backend/src/preprocessing/build_X_actions_weekly.py
python backend/src/preprocessing/build_y_actions_weekly.py

# Calculer les facteurs
python backend/src/factors/compute_momentum.py
python backend/src/factors/compute_volatility.py
python backend/src/factors/compute_sharpe.py

# Créer les datasets
python backend/src/reconstruction/build_reconstruction_dataset.py
python backend/src/ml/build_action_ml_dataset.py
```

Voir [DATA_MANAGEMENT.md](DATA_MANAGEMENT.md) pour plus de détails.

---

## 🛠️ Stack Technique

**Backend** :
- Python 3.10+
- Scikit-learn (Machine Learning)
- CVXPY, Scipy (Optimisation)
- Pandas, Numpy (Data Science)
- Selenium (Web Scraping)

**Frontend** :
- Streamlit (Framework Web)
- Plotly (Visualisations interactives)

**Déploiement** :
- Streamlit Cloud (gratuit)
- GitHub (versioning)

---

## 🎓 Méthodologie

### Reconstruction de Portefeuille

**1. Ridge Regression**
```python
# Minimiser: ||y - Xw||² + α||w||²
# Avec contraintes: Σw = 1, w >= 0
```

**2. SLSQP Optimization**
```python
# Minimiser: Tracking Error²
# Contraintes: Σw = 1, w >= 0 (long-only)
```

### Machine Learning

**Modèle** : Ridge Regression

**Features** :
- Momentum 3M, 6M, 12M
- Volatilité 3M, 6M, 12M
- Sharpe Ratio 3M, 6M, 12M

**Target** : Rendement futur (t+1 semaine)

**Split** : Train/Test temporel (80/20)

---

## 🌐 Déploiement

L'application est déployée sur **Streamlit Cloud** :

**Lien** : [https://votre-app.streamlit.app](#)

Voir [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) pour les instructions complètes.

---

## 📈 Résultats

### Reconstruction WG Actions

- **Tracking Error** : ~1.2% (hebdomadaire)
- **R²** : 0.87
- **Corrélation** : 0.93

### Prédictions ML

- **R² Train** : 0.75
- **R² Test** : 0.45
- **RMSE Test** : 0.008

---

## 👨‍💻 Auteur

**[Votre Nom]**

Challenge Data & AI Internship 2026 - Wafa Gestion

---

## 📜 Licence

Projet académique - Challenge Wafa Gestion 2026

---

## 🙏 Remerciements

- **Wafa Gestion** pour l'organisation du challenge
- **ASFiM** pour les données OPCVM
- **Streamlit** pour la plateforme de déploiement gratuite
