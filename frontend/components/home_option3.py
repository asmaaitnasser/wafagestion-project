"""
Option 3: Business-focused homepage
"""
import streamlit as st

def show():
    # Title
    st.markdown("<h1 style='color: #003A8F;'>🏦 Portfolio Intelligence Platform</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #5B8EDB;'><em>Aide à la décision pour gérants de fonds</em></h3>", unsafe_allow_html=True)

    st.markdown("---")

    # Problem statement
    st.markdown("## 💼 Le Défi")

    st.markdown("""
    <div style='background-color: #F2F2F2; padding: 1.5rem; border-left: 4px solid #C9A227; border-radius: 0.5rem; margin-bottom: 2rem;'>
        <h4 style='margin-top: 0; color: #003A8F;'>🎯 Problème Métier</h4>
        <p style='color: #4D4D4D; margin-bottom: 0;'>
            Les gérants de fonds ont besoin de <strong>comprendre les stratégies concurrentes</strong>
            et d'<strong>identifier les meilleures opportunités d'investissement</strong>,
            mais les OPCVM ne publient que leurs performances, pas leur composition détaillée.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Solution
    st.markdown("## ✨ Notre Solution")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🔍 1. Analyse Concurrentielle

        **Reconstitution de portefeuille** par reverse-engineering :

        - 📊 Algorithmes d'optimisation (Ridge, SLSQP)
        - 🎯 Minimisation de la tracking error
        - 📈 Identification des positions clés
        - 💡 Compréhension des stratégies concurrentes

        **Résultat** : Estimation fiable (R² 0.87) de la composition du fonds WG Actions
        """)

    with col2:
        st.markdown("""
        ### 🚀 2. Recommandations Intelligentes

        **Prédictions ML** pour l'aide à la décision :

        - 🤖 Modèle Ridge sur facteurs techniques
        - 📊 Momentum, Volatilité, Sharpe Ratio
        - 🏆 Top actions recommandées
        - 📉 Backtesting de performance

        **Résultat** : Identification systématique des meilleures opportunités
        """)

    st.markdown("---")

    # Use cases
    st.markdown("## 👥 Pour Qui ?")

    use_cases = [
        {
            "icon": "💼",
            "role": "Gérants de Fonds",
            "use": "Analyser les stratégies concurrentes et ajuster les allocations"
        },
        {
            "icon": "📊",
            "role": "Analystes Quantitatifs",
            "use": "Identifier les opportunités via facteurs techniques et ML"
        },
        {
            "icon": "🛡️",
            "role": "Risk Managers",
            "use": "Vérifier la cohérence entre composition et mandat du fonds"
        },
        {
            "icon": "💹",
            "role": "Traders",
            "use": "Détecter les mouvements de portefeuille et anticiper les flux"
        }
    ]

    cols = st.columns(4)
    for col, uc in zip(cols, use_cases):
        with col:
            st.markdown(f"""
            <div style='text-align: center; padding: 1rem;'>
                <div style='font-size: 2.5rem; margin-bottom: 0.5rem;'>{uc['icon']}</div>
                <div style='font-weight: bold; color: #003A8F; margin-bottom: 0.5rem;'>{uc['role']}</div>
                <div style='font-size: 0.85rem; color: #4D4D4D;'>{uc['use']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # CTA
    st.markdown("## 🎯 Commencer l'Analyse")

    col_left, col_right = st.columns(2)

    with col_left:
        st.info("**🔄 Reconstruction** : Découvrez la composition du portefeuille WG Actions")
        if st.button("▶️ Lancer la Reconstruction", use_container_width=True, type="primary"):
            st.session_state['page'] = "🔄 Reconstruction"
            st.rerun()

    with col_right:
        st.info("**🔮 Prédictions** : Identifiez les meilleures actions à intégrer")
        if st.button("▶️ Voir les Recommandations", use_container_width=True, type="primary"):
            st.session_state['page'] = "🔮 Prédictions ML"
            st.rerun()

    # Impact
    st.markdown("---")
    st.markdown("## 📊 Impact Business")

    impact_cols = st.columns(3)

    with impact_cols[0]:
        st.metric("⏱️ Temps d'Analyse", "60% plus rapide", delta="vs manuel")

    with impact_cols[1]:
        st.metric("🎯 Précision", "87% R²", delta="Tracking Error 1.24%")

    with impact_cols[2]:
        st.metric("💡 Opportunités", "Top 10 actions", delta="Hebdomadaire")
