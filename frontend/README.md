# Wafa Gestion - Portfolio Intelligence Platform (Frontend)

## 🚀 Lancer l'Application Localement

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancer Streamlit
```bash
streamlit run app.py
```

L'application sera accessible sur : http://localhost:8501

## 📊 Pages Disponibles

### 🏠 Accueil
Page d'accueil avec présentation de la plateforme

### 🔄 Reconstruction
- Reconstruction du portefeuille WG Actions
- Méthodes: Ridge Regression, SLSQP
- Visualisations: Pondérations, Tracking Performance
- Export CSV

### 🔮 Prédictions ML
- Top actions recommandées
- Analyse des facteurs techniques
- Prédictions de rendements
- Export CSV

## 🛠️ Structure

```
frontend/
├── app.py                  # Application principale
├── pages/
│   ├── reconstruction.py   # Page reconstruction
│   └── predictions.py      # Page prédictions ML
├── .streamlit/
│   └── config.toml        # Configuration Streamlit
└── requirements.txt       # Dépendances
```

## 🔧 Configuration

Les couleurs et le thème sont configurés dans `.streamlit/config.toml` avec les couleurs de Wafa Gestion (bleu #0066cc).

## 📝 Notes

- L'application importe directement les fonctions du backend (pas d'API REST séparée)
- Les résultats sont stockés dans `st.session_state` pour persister pendant la session
- Compatible avec Streamlit Cloud pour déploiement gratuit
