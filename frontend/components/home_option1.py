"""
Option 1: Dashboard-style homepage with key metrics
"""
import streamlit as st
import pandas as pd
from datetime import datetime

def show():
    # Hero section
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='color: #003A8F; font-size: 2.5rem;'>Portfolio Intelligence Platform</h1>
        <p style='font-size: 1.2rem; color: #5B8EDB;'>Analyse quantitative et optimisation de portefeuilles OPCVM</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📊 Actions Analysées",
            value="15",
            delta="MASI",
            help="Nombre d'actions du marché marocain dans l'analyse"
        )

    with col2:
        st.metric(
            label="🎯 Tracking Error",
            value="1.24%",
            delta="-0.3%",
            delta_color="inverse",
            help="Précision de la reconstruction du portefeuille"
        )

    with col3:
        st.metric(
            label="🤖 Modèle ML",
            value="Ridge",
            delta="R² 0.87",
            help="Modèle de prédiction des rendements"
        )

    with col4:
        st.metric(
            label="📅 Dernière MAJ",
            value=datetime.now().strftime("%d/%m/%Y"),
            help="Dernière mise à jour des données"
        )

    st.markdown("---")

    # Quick actions
    st.markdown("### 🚀 Actions Rapides")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("""
        #### 🔄 Reconstruction de Portefeuille

        Reconstituer le portefeuille **WG Actions** avec :
        - ✅ Ridge Regression (régularisation L2)
        - ✅ SLSQP Optimization (contraintes sum-to-one)
        - ✅ Métriques : R², Tracking Error, Corrélation

        """)
        if st.button("🎯 Commencer la Reconstruction", use_container_width=True, key="btn_reconstruction_home"):
            st.session_state['page'] = "🔄 Reconstruction"
            st.rerun()

    with col_right:
        st.markdown("""
        #### 🔮 Prédictions ML

        Identifier les **meilleures opportunités** d'investissement :
        - ✅ Top actions recommandées (ML)
        - ✅ Facteurs techniques (Momentum, Sharpe, Volatilité)
        - ✅ Backtesting de stratégies

        """)
        if st.button("📈 Voir les Prédictions", use_container_width=True, key="btn_predictions_home"):
            st.session_state['page'] = "🔮 Prédictions ML"
            st.rerun()

    st.markdown("---")

    # Technologies
    st.markdown("### 🛠️ Technologies & Méthodologie")

    tab1, tab2, tab3 = st.tabs(["🧠 Machine Learning", "📐 Optimisation", "📊 Données"])

    with tab1:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("**Modèle**")
            st.code("Ridge Regression", language="text")
        with col2:
            st.markdown("**Features**")
            st.markdown("- Momentum 3M/6M/12M\n- Volatilité 3M/6M/12M\n- Sharpe Ratio 3M/6M/12M")

    with tab2:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("**Algorithmes**")
            st.code("SLSQP / Ridge", language="text")
        with col2:
            st.markdown("**Contraintes**")
            st.markdown("- Σw = 1 (full investment)\n- w ≥ 0 (long-only)")

    with tab3:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("**Source**")
            st.code("ASFiM (OPCVM)", language="text")
        with col2:
            st.markdown("**Période**")
            st.markdown("- Historique : 2023-2025\n- Fréquence : Hebdomadaire")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #4D4D4D; padding: 1rem 0;'>
        <p>📊 Challenge Data & AI 2026 - Wafa Gestion</p>
        <p style='font-size: 0.9rem;'>Développé avec Python, Streamlit, Scikit-learn & CVXPY</p>
    </div>
    """, unsafe_allow_html=True)
