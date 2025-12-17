# 🚀 Guide de Déploiement - Streamlit Cloud

## Prérequis

- ✅ Compte GitHub (gratuit)
- ✅ Compte Streamlit Cloud (gratuit) : https://streamlit.io/cloud
- ✅ Projet poussé sur GitHub

## Étapes de Déploiement (15 minutes)

### 1️⃣ Préparer le Repository GitHub

```bash
# Assurez-vous que tout est commité
git status
git add .
git commit -m "feat: Add Streamlit web application for Wafa Gestion challenge"
git push origin main
```

### 2️⃣ Créer un fichier requirements.txt à la racine

Le fichier `requirements.txt` à la racine du projet doit contenir TOUTES les dépendances (backend + frontend).

**Fichier déjà créé** : `requirements.txt` (racine du projet)

Vérifiez qu'il contient :
```
streamlit>=1.28.0
plotly>=5.17.0
pandas>=2.1.0
numpy>=1.24.0
scikit-learn>=1.3.0
scipy>=1.11.0
cvxpy>=1.4.0
openpyxl
```

### 3️⃣ Créer un fichier de configuration Streamlit Cloud (optionnel)

Créez `.streamlit/config.toml` à la racine si ce n'est pas déjà fait :

```toml
[theme]
primaryColor = "#0066cc"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
enableCORS = false
```

### 4️⃣ Se Connecter à Streamlit Cloud

1. Aller sur : https://streamlit.io/cloud
2. Cliquer sur "Sign up with GitHub"
3. Autoriser Streamlit à accéder à vos repositories

### 5️⃣ Déployer l'Application

1. Cliquer sur "New app"
2. Sélectionner votre repository : `votre-username/wafagestion`
3. **Branch** : `main`
4. **Main file path** : `frontend/app.py`
5. Cliquer sur "Deploy!"

⏳ Le déploiement prend 2-5 minutes.

### 6️⃣ Obtenir le Lien Public

Une fois déployé, vous obtiendrez un lien du type :
```
https://votre-app-name.streamlit.app
```

**Copiez ce lien** - c'est celui que vous soumettrez au jury !

## 🔧 Résolution de Problèmes

### Erreur : "File not found"

**Solution** : Vérifiez le chemin du fichier principal dans les paramètres Streamlit Cloud.
Il doit être : `frontend/app.py`

### Erreur : "Module not found"

**Solution** : Vérifiez que `requirements.txt` contient toutes les dépendances.

Vous pouvez régénérer le fichier :
```bash
pip freeze > requirements.txt
```

### Erreur : "Data files not found"

**Solution** : Les fichiers de données volumineux ne sont pas sur GitHub (gitignore).

**Options** :
1. Utiliser des données d'exemple plus petites
2. Télécharger les données au premier lancement de l'app
3. Utiliser Streamlit Secrets pour stocker un lien Google Drive

**Pour le challenge, option 1 est recommandée** : Créez des fichiers CSV d'exemple légers.

### Application très lente

**Causes possibles** :
- Fichiers de données trop volumineux
- Calculs trop lourds à chaque interaction

**Solutions** :
- Utiliser `@st.cache_data` pour mettre en cache les résultats
- Limiter la taille des datasets

## 📊 Optimisations pour Streamlit Cloud

### Ajouter du caching (important !)

Dans `frontend/pages/reconstruction.py`, ajoutez :

```python
@st.cache_data
def load_data():
    # Charger les données une seule fois
    return pd.read_csv("backend/data/processed/Y_fund_weekly.csv")
```

### Limiter la taille des données

Pour le démo, utilisez seulement les 100 dernières lignes :

```python
df = pd.read_csv("data.csv").tail(100)
```

## 🎯 Checklist Finale Avant Soumission

- [ ] Application déployée et accessible via lien public
- [ ] Toutes les pages fonctionnent (Accueil, Reconstruction, Prédictions)
- [ ] Pas d'erreur dans les logs Streamlit Cloud
- [ ] Design professionnel (couleurs Wafa Gestion)
- [ ] Screenshots pris pour la présentation
- [ ] Vidéo démo enregistrée (2-3 min)
- [ ] Lien testé en navigation privée (vérifier accessibilité publique)

## 🎬 Pour la Soumission (22/12/2025)

### Dossier Google Drive doit contenir :

1. ✅ **Présentation PPT** : `WafaGestion_Challenge_VotreNom.pptx`
2. ✅ **Lien déployé** : Dans un fichier `LIEN_APP.txt`
   ```
   Lien de l'application :
   https://votre-app.streamlit.app

   Repository GitHub :
   https://github.com/votre-username/wafagestion
   ```
3. ✅ **Screenshots** : Dossier avec 5-10 captures d'écran
4. ✅ **Vidéo démo** : `demo.mp4` (ou lien YouTube si >50MB)
5. ✅ **CV** : `CV_VotreNom.pdf`

## 🆘 Support

- **Documentation Streamlit** : https://docs.streamlit.io/
- **Forum Streamlit** : https://discuss.streamlit.io/
- **Streamlit Cloud Docs** : https://docs.streamlit.io/streamlit-community-cloud

## 🎉 Bon Déploiement !
