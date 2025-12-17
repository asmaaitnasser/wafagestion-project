"""
Option 2: Minimalist landing page
"""
import streamlit as st

def show():
    # Hero avec image de fond (style)
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #003A8F 0%, #5B8EDB 100%);
        padding: 4rem 2rem;
        border-radius: 1rem;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    '>
        <h1 style='font-size: 3rem; margin-bottom: 1rem; font-weight: 700;'>
            Portfolio Intelligence
        </h1>
        <p style='font-size: 1.3rem; opacity: 0.95; margin-bottom: 2rem;'>
            Optimisez vos investissements avec l'IA et l'analyse quantitative
        </p>
        <p style='font-size: 1rem; opacity: 0.8;'>
            🏦 Wafa Gestion - Challenge Data & AI 2026
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Value propositions
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 2rem 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>🔄</div>
            <h3 style='color: #003A8F;'>Reconstruction</h3>
            <p style='color: #4D4D4D;'>
                Découvrez la composition réelle des portefeuilles OPCVM grâce à des algorithmes d'optimisation avancés.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 2rem 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>🤖</div>
            <h3 style='color: #003A8F;'>Prédictions ML</h3>
            <p style='color: #4D4D4D;'>
                Identifiez les meilleures opportunités avec notre modèle de Machine Learning entraîné sur des facteurs techniques.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style='text-align: center; padding: 2rem 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 1rem;'>📊</div>
            <h3 style='color: #003A8F;'>Analytics</h3>
            <p style='color: #4D4D4D;'>
                Visualisations interactives et métriques avancées pour une analyse approfondie de la performance.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # CTA buttons
    col_space1, col_cta1, col_cta2, col_space2 = st.columns([1, 2, 2, 1])

    with col_cta1:
        if st.button("🎯 Reconstruire un Portefeuille", use_container_width=True, type="primary"):
            st.session_state['page'] = "🔄 Reconstruction"
            st.rerun()

    with col_cta2:
        if st.button("📈 Voir les Prédictions", use_container_width=True):
            st.session_state['page'] = "🔮 Prédictions ML"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Stats section
    st.markdown("""
    <div style='background-color: #F2F2F2; padding: 2rem; border-radius: 1rem; margin-top: 3rem;'>
        <h3 style='text-align: center; margin-bottom: 2rem; color: #003A8F;'>📊 Chiffres Clés</h3>
    </div>
    """, unsafe_allow_html=True)

    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

    stats = [
        ("15", "Actions MASI", "📈"),
        ("87%", "Précision R²", "🎯"),
        ("1.24%", "Tracking Error", "📉"),
        ("2023-2025", "Période", "📅")
    ]

    for col, (value, label, icon) in zip([stat_col1, stat_col2, stat_col3, stat_col4], stats):
        with col:
            st.markdown(f"""
            <div style='text-align: center;'>
                <div style='font-size: 2rem;'>{icon}</div>
                <div style='font-size: 2rem; font-weight: bold; color: #003A8F;'>{value}</div>
                <div style='color: #4D4D4D;'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; color: #999; border-top: 1px solid #ddd; padding-top: 2rem; margin-top: 2rem;'>
        <p>Développé avec ❤️ pour le Challenge Data & AI 2026</p>
        <p style='font-size: 0.85rem;'>Python • Streamlit • Scikit-learn • CVXPY • Plotly</p>
    </div>
    """, unsafe_allow_html=True)
