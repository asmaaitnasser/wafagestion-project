"""
Page 2: ML Predictions
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path for utils import
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.import_helper import import_ml_predictor

# Import backend classes
MLPredictor = import_ml_predictor()


def show():
    # Enhanced Header Section
    st.markdown("""
        <div class="gradient-card animate-fadeIn" style='
            padding: 2.5rem;
            margin-bottom: 2rem;
            border-radius: 20px;
            background: linear-gradient(135deg, #10B981 0%, #34D399 50%, #6EE7B7 100%);
            background-size: 200% 200%;
            animation: gradient-shift 8s ease infinite;
        '>
            <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                <div style='
                    width: 60px;
                    height: 60px;
                    background: rgba(255, 255, 255, 0.2);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 2rem;
                '>🔮</div>
                <div>
                    <h1 style='color: white; margin: 0; font-size: 2.5rem; font-weight: 800;'>
                        Prédictions ML & Recommandations
                    </h1>
                    <p style='color: rgba(255, 255, 255, 0.9); margin: 0.5rem 0 0 0; font-size: 1.1rem;'>
                        Intelligence Artificielle pour l'Investissement
                    </p>
                </div>
            </div>
            <div style='
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(10px);
                padding: 1rem 1.5rem;
                border-radius: 12px;
                margin-top: 1rem;
            '>
                <p style='color: white; margin: 0; font-size: 1rem; line-height: 1.6;'>
                    Utilisez le <strong>Machine Learning</strong> pour prédire les rendements futurs des actions
                    et identifier les meilleures opportunités d'investissement.
                </p>
                <p style='color: rgba(255, 255, 255, 0.9); margin: 0.5rem 0 0 0; font-size: 0.95rem;'>
                    <strong>Modèle</strong> : Ridge Regression avec facteurs techniques (Momentum, Volatilité, Sharpe Ratio)
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Back button
    if st.button("← Retour à l'accueil", key="back_to_home_predictions", use_container_width=False):
        st.session_state['page'] = "🏠 Accueil"
        st.rerun()

    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    # Enhanced Parameters Section
    st.markdown("""
        <div class="custom-card animate-slideUp" style='margin-bottom: 2rem;'>
            <h2 style='color: #003A8F; font-size: 1.75rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.75rem;'>
                <span style='font-size: 2rem;'>⚙️</span>
                Paramètres de Prédiction
            </h2>
    """, unsafe_allow_html=True)

    col_slider, col_info = st.columns([2, 1])

    with col_slider:
        n_top = st.slider(
            "Nombre de recommandations",
            min_value=3,
            max_value=20,
            value=10,
            help="Nombre d'actions à recommander",
            key="n_top_slider"
        )

    with col_info:
        st.markdown("""
            <div style='
                background: linear-gradient(135deg, rgba(0, 58, 143, 0.05) 0%, rgba(91, 142, 219, 0.05) 100%);
                padding: 1.5rem;
                border-radius: 12px;
                border-left: 4px solid #10B981;
            '>
                <div style='font-size: 1.5rem; margin-bottom: 0.5rem;'>💡</div>
                <div style='font-weight: 600; color: #003A8F; margin-bottom: 0.5rem;'>Astuce</div>
                <div style='color: #4D4D4D; font-size: 0.9rem;'>
                    Plus de recommandations = analyse plus complète mais moins précise
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Enhanced Action Button
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    if st.button("🚀 Générer les Prédictions", type="primary", use_container_width=True):

        with st.spinner("⏳ Génération des prédictions..."):
            # Appel au backend
            predictions = MLPredictor.get_top_predictions(n_top=n_top)

        if predictions.empty:
            st.error("❌ Aucune donnée disponible pour les prédictions. Assurez-vous que le dataset ML existe.")
            st.stop()

        # Store in session
        st.session_state['predictions'] = predictions

    # Display results
    if 'predictions' in st.session_state:
        predictions = st.session_state['predictions']

        st.markdown("""
            <div style='
                background: linear-gradient(135deg, #10B981 0%, #34D399 100%);
                color: white;
                padding: 1.5rem;
                border-radius: 16px;
                margin: 1.5rem 0;
                box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3);
                animation: slideUp 0.5s ease-out;
            '>
                <div style='display: flex; align-items: center; gap: 1rem;'>
                    <span style='font-size: 2.5rem;'>✅</span>
                    <div>
                        <h3 style='margin: 0; font-size: 1.5rem;'>Prédictions générées avec succès !</h3>
                        <p style='margin: 0.5rem 0 0 0; opacity: 0.95;'>Les recommandations sont disponibles ci-dessous</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style='
                background: white;
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
            '>
                <h2 style='color: #003A8F; font-size: 2rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.75rem;'>
                    <span style='font-size: 2.5rem;'>🏆</span>
                    Top Actions Recommandées
                </h2>
        """, unsafe_allow_html=True)

        # Enhanced Top 3 Display with Cards
        medals = ["🥇", "🥈", "🥉"]
        medal_colors = ["#FFD700", "#C0C0C0", "#CD7F32"]
        
        for position, (idx, row) in enumerate(predictions.head(3).iterrows()):
            medal = medals[position]
            medal_color = medal_colors[position]
            pred_value = row['Predicted_Return']
            is_positive = pred_value > 0
            
            st.markdown(f"""
                <div class="custom-card animate-slideUp" style='
                    margin-bottom: 1rem;
                    border-left: 5px solid {medal_color};
                    animation-delay: {position * 0.1}s;
                '>
                    <div style='display: flex; align-items: center; gap: 1.5rem;'>
                        <div style='
                            font-size: 4rem;
                            line-height: 1;
                        '>{medal}</div>
                        <div style='flex: 1;'>
                            <h3 style='
                                color: #003A8F;
                                font-size: 2rem;
                                margin: 0 0 0.5rem 0;
                                font-weight: 800;
                            '>{row['Ticker']}</h3>
                            <div style='
                                display: flex;
                                gap: 1rem;
                                flex-wrap: wrap;
                            '>
                                <span style='
                                    background: rgba(0, 58, 143, 0.1);
                                    color: #003A8F;
                                    padding: 0.5rem 1rem;
                                    border-radius: 8px;
                                    font-size: 0.9rem;
                                    font-weight: 600;
                                '>
                                    Momentum 3M: {row.get('Momentum_3M', 0):.2%}
                                </span>
                            </div>
                        </div>
                        <div style='
                            text-align: right;
                            padding: 1rem;
                            background: {'linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(52, 211, 153, 0.1) 100%)' if is_positive else 'linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(248, 113, 113, 0.1) 100%)'};
                            border-radius: 12px;
                            min-width: 150px;
                        '>
                            <div style='
                                color: {'#10B981' if is_positive else '#EF4444'};
                                font-size: 2rem;
                                font-weight: 800;
                                margin-bottom: 0.25rem;
                            '>
                                {pred_value:.4f}
                            </div>
                            <div style='
                                color: #4D4D4D;
                                font-size: 0.85rem;
                            '>
                                Rendement prédit (hebdomadaire)
                            </div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

        # Enhanced Visualizations Section
        st.markdown("""
            <div style='
                background: white;
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
            '>
                <h2 style='color: #003A8F; font-size: 1.75rem; margin-bottom: 1.5rem;'>
                    📊 Visualisations Interactives
                </h2>
        """, unsafe_allow_html=True)

        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("#### 📊 Classement des Prédictions")

            # Enhanced Bar chart with better styling
            fig_bar = go.Figure(go.Bar(
                x=predictions['Predicted_Return'].values,
                y=predictions['Ticker'].values,
                orientation='h',
                marker=dict(
                    color=predictions['Predicted_Return'].values,
                    colorscale=[[0, '#EF4444'], [0.3, '#F59E0B'], [0.5, '#F2F2F2'], [0.7, '#10B981'], [1, '#C9A227']],
                    showscale=True,
                    colorbar=dict(
                        title=dict(text="Rendement Prédit", font=dict(color='#003A8F', family='Inter')),
                        tickfont=dict(color='#4D4D4D', family='Inter')
                    ),
                    line=dict(color='white', width=1)
                ),
                text=[f"{v:.4f}" for v in predictions['Predicted_Return'].values],
                textposition='auto',
                textfont=dict(color='white', size=11, family='Inter'),
                hovertemplate='<b>%{y}</b><br>Rendement Prédit: %{x:.4f}<extra></extra>'
            ))

            fig_bar.update_layout(
                xaxis_title="Rendement Prédit",
                yaxis_title="Action",
                height=550,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#4D4D4D'),
                margin=dict(l=20, r=20, t=20, b=20),
                xaxis=dict(
                    gridcolor='rgba(0, 0, 0, 0.05)',
                    showgrid=True
                ),
                yaxis=dict(
                    autorange="reversed",
                    gridcolor='rgba(0, 0, 0, 0.05)',
                    showgrid=True
                )
            )

            st.plotly_chart(fig_bar, use_container_width=True)

        with col_right:
            st.markdown("#### 🎯 Analyse des Facteurs")

            # Enhanced Scatter plot
            if 'Momentum_3M' in predictions.columns and 'Volatility_3M' in predictions.columns:
                fig_scatter = px.scatter(
                    predictions,
                    x='Momentum_3M',
                    y='Predicted_Return',
                    size='Volatility_3M' if 'Volatility_3M' in predictions.columns else None,
                    color='Predicted_Return',
                    hover_data=['Ticker'],
                    color_continuous_scale=[[0, '#EF4444'], [0.3, '#F59E0B'], [0.5, '#F2F2F2'], [0.7, '#10B981'], [1, '#C9A227']],
                    labels={
                        'Momentum_3M': 'Momentum 3 Mois',
                        'Predicted_Return': 'Rendement Prédit',
                        'Volatility_3M': 'Volatilité 3M'
                    },
                    hover_name='Ticker'
                )

                fig_scatter.update_layout(
                    height=550,
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(family='Inter', color='#4D4D4D'),
                    margin=dict(l=20, r=20, t=20, b=20),
                    xaxis=dict(
                        gridcolor='rgba(0, 0, 0, 0.05)',
                        showgrid=True
                    ),
                    yaxis=dict(
                        gridcolor='rgba(0, 0, 0, 0.05)',
                        showgrid=True
                    )
                )
                
                st.plotly_chart(fig_scatter, use_container_width=True)
            else:
                st.markdown("""
                    <div style='
                        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(147, 197, 253, 0.1) 100%);
                        padding: 2rem;
                        border-radius: 12px;
                        border-left: 4px solid #3B82F6;
                        text-align: center;
                    '>
                        <div style='font-size: 3rem; margin-bottom: 1rem;'>ℹ️</div>
                        <p style='color: #4D4D4D; margin: 0;'>
                            Les données de facteurs (Momentum, Volatilité) ne sont pas disponibles pour l'affichage.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

        # Enhanced Detailed Table Section
        st.markdown("""
            <div style='
                background: white;
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
            '>
                <h2 style='color: #003A8F; font-size: 1.75rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.75rem;'>
                    <span style='font-size: 2rem;'>📋</span>
                    Tableau Détaillé des Prédictions
                </h2>
        """, unsafe_allow_html=True)

        # Format for display
        display_df = predictions.copy()
        if 'Predicted_Return' in display_df.columns:
            display_df['Rendement Prédit (%)'] = display_df['Predicted_Return'].apply(lambda x: f"{x:.4%}")

        st.dataframe(
            display_df,
            use_container_width=True,
            height=400
        )
        
        st.markdown("</div>", unsafe_allow_html=True)

        # Informations additionnelles
        with st.expander("📚 Méthodologie & Facteurs Utilisés"):
            st.markdown("""
            ### Facteurs Techniques

            **Momentum**
            - Momentum 3 mois, 6 mois, 12 mois
            - Calcule la tendance des rendements récents

            **Volatilité**
            - Volatilité 3M, 6M, 12M
            - Mesure le risque de l'action

            **Sharpe Ratio**
            - Ratio rendement/risque
            - Indicateur de performance ajustée au risque

            ### Modèle ML

            **Ridge Regression**
            - Régression linéaire avec régularisation L2
            - Évite l'overfitting
            - Split train/test: 80/20 temporel
            """)

        # Enhanced Export Section
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        col_export, col_warning = st.columns([1, 1])
        
        with col_export:
            csv_pred = predictions.to_csv(index=False)
            st.download_button(
                label="📥 Télécharger les Prédictions (CSV)",
                data=csv_pred,
                file_name="ml_predictions.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col_warning:
            st.markdown("""
                <div style='
                    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(251, 191, 36, 0.1) 100%);
                    padding: 1.5rem;
                    border-radius: 12px;
                    border-left: 4px solid #F59E0B;
                '>
                    <div style='font-size: 1.5rem; margin-bottom: 0.5rem;'>⚠️</div>
                    <div style='font-weight: 600; color: #003A8F; margin-bottom: 0.5rem;'>Disclaimer</div>
                    <p style='color: #4D4D4D; margin: 0; font-size: 0.9rem; line-height: 1.5;'>
                        Ces prédictions sont basées sur des modèles statistiques et ne constituent pas
                        des conseils d'investissement. Les performances passées ne préjugent pas des performances futures.
                    </p>
                </div>
            """, unsafe_allow_html=True)
