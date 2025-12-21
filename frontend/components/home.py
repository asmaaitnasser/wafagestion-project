"""
Page d'accueil - Design Premium
Wafa Gestion Portfolio Intelligence Platform
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def show():
    """Display premium homepage"""

    # Hero Section with Enhanced Gradient and Animations
    st.markdown("""
        <div class="gradient-card animate-fadeIn" style='
            background: linear-gradient(135deg, #003A8F 0%, #5B8EDB 50%, #7FA8E5 100%);
            background-size: 200% 200%;
            animation: gradient-shift 8s ease infinite;
            color: white;
            text-align: center;
            padding: 5rem 2rem;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
            border-radius: 24px;
            box-shadow: 0 20px 60px rgba(0, 58, 143, 0.3);
        '>
            <div style='position: relative; z-index: 1;'>
                <h1 style='
                    font-size: 3.5rem; 
                    font-weight: 900; 
                    margin-bottom: 1rem; 
                    line-height: 1.2;
                    text-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                    animation: fadeInScale 0.8s ease-out;
                '>
                    Portfolio Intelligence Platform
                </h1>
                <p style='
                    font-size: 1.35rem; 
                    opacity: 0.95; 
                    max-width: 800px; 
                    margin: 0 auto 2.5rem auto; 
                    line-height: 1.7;
                    animation: slideUp 1s ease-out;
                '>
                    Reconstituez et optimisez vos portefeuilles OPCVM grâce au Machine Learning et aux algorithmes d'optimisation quantitative
                </p>
                <div style='
                    display: flex; 
                    gap: 1rem; 
                    justify-content: center; 
                    flex-wrap: wrap;
                    animation: slideUp 1.2s ease-out;
                '>
                    <span class='badge-gold animate-float' style='
                        padding: 0.875rem 1.75rem; 
                        font-size: 1rem;
                        border-radius: 50px;
                        box-shadow: 0 4px 12px rgba(201, 162, 39, 0.3);
                        transition: all 0.3s ease;
                    '>
                        🎯 Tracking Error < 1.5%
                    </span>
                    <span class='badge-gold animate-float' style='
                        padding: 0.875rem 1.75rem; 
                        font-size: 1rem;
                        border-radius: 50px;
                        box-shadow: 0 4px 12px rgba(201, 162, 39, 0.3);
                        animation-delay: 0.2s;
                        transition: all 0.3s ease;
                    '>
                        🚀 R² > 0.85
                    </span>
                    <span class='badge-gold animate-float' style='
                        padding: 0.875rem 1.75rem; 
                        font-size: 1rem;
                        border-radius: 50px;
                        box-shadow: 0 4px 12px rgba(201, 162, 39, 0.3);
                        animation-delay: 0.4s;
                        transition: all 0.3s ease;
                    '>
                        🎓 ML-Powered
                    </span>
                </div>
            </div>
            <!-- Animated background elements -->
            <div style='
                position: absolute;
                top: -30%;
                right: -10%;
                width: 600px;
                height: 600px;
                background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
                border-radius: 50%;
                animation: pulse 4s ease-in-out infinite;
            '></div>
            <div style='
                position: absolute;
                bottom: -20%;
                left: -5%;
                width: 400px;
                height: 400px;
                background: radial-gradient(circle, rgba(201, 162, 39, 0.1) 0%, transparent 70%);
                border-radius: 50%;
                animation: pulse 5s ease-in-out infinite;
                animation-delay: 1s;
            '></div>
        </div>
    """, unsafe_allow_html=True)

    # Key Features in 3 Columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="custom-card animate-slideUp" style='
                height: 100%; 
                text-align: center;
                cursor: pointer;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            ' onmouseover="this.style.transform='translateY(-8px) scale(1.02)'" onmouseout="this.style.transform='translateY(0) scale(1)'">
                <div style='
                    width: 90px;
                    height: 90px;
                    background: linear-gradient(135deg, #003A8F 0%, #5B8EDB 100%);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1.5rem auto;
                    font-size: 2.75rem;
                    box-shadow: 0 8px 20px rgba(0, 58, 143, 0.3);
                    transition: all 0.3s ease;
                    animation: float 3s ease-in-out infinite;
                '>
                    🔄
                </div>
                <h3 style='
                    color: #003A8F; 
                    font-size: 1.6rem; 
                    margin-bottom: 1rem;
                    font-weight: 700;
                '>
                    Reconstruction
                </h3>
                <p style='color: #4D4D4D; line-height: 1.7; font-size: 1rem;'>
                    Reconstituez la composition d'un OPCVM avec une précision de <strong style='color: #003A8F;'>93%</strong>
                    grâce à Ridge Regression et SLSQP
                </p>
                <div style='
                    margin-top: 1.5rem; 
                    padding-top: 1.5rem; 
                    border-top: 2px solid #F2F2F2;
                '>
                    <div style='color: #003A8F; font-size: 0.875rem; font-weight: 600; margin-bottom: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px;'>
                        Algorithmes
                    </div>
                    <span class='badge badge-info' style='margin: 0.25rem; padding: 0.5rem 1rem;'>Ridge</span>
                    <span class='badge badge-info' style='margin: 0.25rem; padding: 0.5rem 1rem;'>SLSQP</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="custom-card animate-slideUp" style='
                height: 100%; 
                text-align: center; 
                animation-delay: 0.1s;
                cursor: pointer;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            ' onmouseover="this.style.transform='translateY(-8px) scale(1.02)'" onmouseout="this.style.transform='translateY(0) scale(1)'">
                <div style='
                    width: 90px;
                    height: 90px;
                    background: linear-gradient(135deg, #10B981 0%, #34D399 100%);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1.5rem auto;
                    font-size: 2.75rem;
                    box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3);
                    transition: all 0.3s ease;
                    animation: float 3s ease-in-out infinite;
                    animation-delay: 0.2s;
                '>
                    🔮
                </div>
                <h3 style='
                    color: #003A8F; 
                    font-size: 1.6rem; 
                    margin-bottom: 1rem;
                    font-weight: 700;
                '>
                    Prédictions ML
                </h3>
                <p style='color: #4D4D4D; line-height: 1.7; font-size: 1rem;'>
                    Identifiez les meilleures opportunités d'investissement avec un modèle ML
                    basé sur <strong style='color: #10B981;'>9 facteurs techniques</strong>
                </p>
                <div style='
                    margin-top: 1.5rem; 
                    padding-top: 1.5rem; 
                    border-top: 2px solid #F2F2F2;
                '>
                    <div style='color: #003A8F; font-size: 0.875rem; font-weight: 600; margin-bottom: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px;'>
                        Facteurs
                    </div>
                    <span class='badge badge-success' style='margin: 0.25rem; padding: 0.5rem 1rem;'>Momentum</span>
                    <span class='badge badge-warning' style='margin: 0.25rem; padding: 0.5rem 1rem;'>Volatilité</span>
                    <span class='badge badge-info' style='margin: 0.25rem; padding: 0.5rem 1rem;'>Sharpe</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="custom-card animate-slideUp" style='
                height: 100%; 
                text-align: center; 
                animation-delay: 0.2s;
                cursor: pointer;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            ' onmouseover="this.style.transform='translateY(-8px) scale(1.02)'" onmouseout="this.style.transform='translateY(0) scale(1)'">
                <div style='
                    width: 90px;
                    height: 90px;
                    background: linear-gradient(135deg, #C9A227 0%, #FFD700 100%);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 1.5rem auto;
                    font-size: 2.75rem;
                    box-shadow: 0 8px 20px rgba(201, 162, 39, 0.3);
                    transition: all 0.3s ease;
                    animation: float 3s ease-in-out infinite;
                    animation-delay: 0.4s;
                '>
                    📊
                </div>
                <h3 style='
                    color: #003A8F; 
                    font-size: 1.6rem; 
                    margin-bottom: 1rem;
                    font-weight: 700;
                '>
                    Analytics
                </h3>
                <p style='color: #4D4D4D; line-height: 1.7; font-size: 1rem;'>
                    Visualisations interactives et métriques en temps réel pour une prise
                    de décision <strong style='color: #C9A227;'>data-driven</strong>
                </p>
                <div style='
                    margin-top: 1.5rem; 
                    padding-top: 1.5rem; 
                    border-top: 2px solid #F2F2F2;
                '>
                    <div style='color: #003A8F; font-size: 0.875rem; font-weight: 600; margin-bottom: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px;'>
                        Outils
                    </div>
                    <span class='badge badge-info' style='margin: 0.25rem; padding: 0.5rem 1rem;'>Plotly</span>
                    <span class='badge badge-info' style='margin: 0.25rem; padding: 0.5rem 1rem;'>Export CSV</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)

    # Performance Metrics Section
    st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h2 style='font-size: 2.25rem; font-weight: 800; color: #003A8F; margin-bottom: 0.5rem;'>
                Performance du Modèle
            </h2>
            <p style='font-size: 1.1rem; color: #4D4D4D; max-width: 700px; margin: 0 auto;'>
                Résultats obtenus sur le fonds <strong>WG Actions</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Metrics Cards with enhanced animations
    col1, col2, col3, col4 = st.columns(4)

    metrics_data = [
        {"label": "R² Score", "value": "0.87", "delta": "▲ Excellent fit", "color": "#10B981"},
        {"label": "Tracking Error", "value": "1.2%", "delta": "▼ Très faible", "color": "#10B981"},
        {"label": "Corrélation", "value": "0.93", "delta": "▲ Très forte", "color": "#10B981"},
        {"label": "ML R² Test", "value": "0.45", "delta": "✓ Robuste", "color": "#10B981"}
    ]

    for idx, (col, metric) in enumerate(zip([col1, col2, col3, col4], metrics_data)):
        with col:
            st.markdown(f"""
                <div class="metric-card animate-slideUp" style='
                    animation-delay: {idx * 0.1}s;
                    cursor: pointer;
                ' onmouseover="this.style.transform='translateY(-6px) scale(1.05)'" onmouseout="this.style.transform='translateY(0) scale(1)'">
                    <div class="metric-label">{metric['label']}</div>
                    <div class="metric-value" style='color: {metric['color']};'>{metric['value']}</div>
                    <div class="metric-delta positive" style='color: {metric['color']};'>
                        {metric['delta']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)

    # Workflow Section
    st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h2 style='font-size: 2.25rem; font-weight: 800; color: #003A8F; margin-bottom: 0.5rem;'>
                Comment ça marche ?
            </h2>
        </div>
    """, unsafe_allow_html=True)

    # Workflow Steps
    col1, col2, col3, col4, col5 = st.columns(5)

    steps = [
        ("📥", "Scraping", "Collecte des données ASFiM", col1),
        ("🔧", "Processing", "Nettoyage & features", col2),
        ("🤖", "Modélisation", "Ridge ML + SLSQP", col3),
        ("📊", "Analytics", "Visualisations", col4),
        ("💡", "Insights", "Décisions", col5)
    ]

    for icon, title, desc, col in steps:
        with col:
            st.markdown(f"""
                <div style='
                    background: white;
                    border-radius: 16px;
                    padding: 1.5rem 1rem;
                    text-align: center;
                    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                    border: 2px solid transparent;
                    transition: all 0.3s ease;
                    height: 100%;
                ' class='custom-card'>
                    <div style='font-size: 3rem; margin-bottom: 0.75rem;'>{icon}</div>
                    <div style='font-weight: 700; color: #003A8F; margin-bottom: 0.5rem; font-size: 1rem;'>
                        {title}
                    </div>
                    <div style='font-size: 0.85rem; color: #4D4D4D;'>
                        {desc}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)

    # CTA Section
    st.markdown("""
        <div class="gradient-card animate-fadeIn" style='text-align: center; padding: 3rem 2rem;'>
            <h2 style='font-size: 2rem; font-weight: 800; margin-bottom: 1rem;'>
                Prêt à explorer ?
            </h2>
            <p style='font-size: 1.1rem; opacity: 0.95; margin-bottom: 2rem; max-width: 600px; margin-left: auto; margin-right: auto;'>
                Utilisez la navigation à gauche pour accéder aux fonctionnalités de reconstruction
                et de prédictions ML
            </p>
            <div style='display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;'>
                <div style='
                    background: white;
                    color: #003A8F;
                    padding: 1rem 2rem;
                    border-radius: 12px;
                    font-weight: 700;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    display: inline-block;
                '>
                    🔄 Reconstruction de Portefeuille
                </div>
                <div style='
                    background: rgba(255, 255, 255, 0.2);
                    color: white;
                    padding: 1rem 2rem;
                    border-radius: 12px;
                    font-weight: 700;
                    border: 2px solid white;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    display: inline-block;
                '>
                    🔮 Prédictions ML
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

    # Tech Stack Details
    with st.expander("🔧 Stack Technique Détaillé", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                **Backend**
                - Python 3.10+
                - Scikit-learn (Machine Learning)
                - CVXPY (Optimisation)
                - Pandas & Numpy
                - Selenium (Scraping)
            """)

        with col2:
            st.markdown("""
                **Frontend**
                - Streamlit 1.28+
                - Plotly (Graphiques)
                - Custom CSS
                - Responsive Design
            """)

    # Data Source
    with st.expander("📊 Source des Données", expanded=False):
        st.markdown("""
            **ASFiM** (Association des Sociétés de Gestion et Fonds d'Investissement Marocains)

            - 📅 **Période**: 2024-2025 (100+ semaines)
            - 📈 **Fonds**: WG Actions + 15 actions individuelles
            - 🔄 **Fréquence**: Données hebdomadaires
            - 🎯 **Fiabilité**: Données publiques officielles

            **Actions incluses**: ATW, BOA, CDM, CIH, CSR, GAZ, HPS, IAM, LBV, LSE, LHF, MNG, SID, TQM, WAA
        """)
