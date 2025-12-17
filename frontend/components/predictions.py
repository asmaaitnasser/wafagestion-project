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
    # Back button
    if st.button("← Retour à l'accueil", key="back_to_home_predictions"):
        st.session_state['page'] = "🏠 Accueil"
        st.rerun()

    st.markdown("## 🔮 Prédictions ML & Recommandations d'Investissement")

    st.markdown("""
    Cette page utilise le **Machine Learning** pour prédire les rendements futurs des actions
    et identifier les meilleures opportunités d'investissement.

    **Modèle** : Ridge Regression avec facteurs techniques (Momentum, Volatilité, Sharpe Ratio)
    """)

    st.markdown("---")

    # Paramètres
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### ⚙️ Paramètres de Prédiction")

    n_top = st.slider(
        "Nombre de recommandations",
        min_value=3,
        max_value=20,
        value=10,
        help="Nombre d'actions à recommander"
    )

    # Bouton prédiction
    st.markdown("---")

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

        st.success("✅ Prédictions générées avec succès !")

        st.markdown("---")
        st.markdown("### 🏆 Top Actions Recommandées")

        # Display top recommendations with medals
        for idx, row in predictions.head(3).iterrows():
            medal = ["🥇", "🥈", "🥉"][idx] if idx < 3 else f"#{idx+1}"

            col_medal, col_ticker, col_pred = st.columns([0.5, 2, 2])

            with col_medal:
                st.markdown(f"## {medal}")

            with col_ticker:
                st.markdown(f"### {row['Ticker']}")
                if 'Momentum_3M' in row:
                    st.caption(f"Momentum 3M: {row.get('Momentum_3M', 0):.2%}")

            with col_pred:
                pred_value = row['Predicted_Return']
                color = "green" if pred_value > 0 else "red"
                st.markdown(f"### :{color}[{pred_value:.4f}]")
                st.caption("Rendement prédit (hebdomadaire)")

        st.markdown("---")

        # Visualizations
        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("#### 📊 Classement des Prédictions")

            # Bar chart - Wafa Gestion colors
            # Custom color scale: dark blue (negative) -> gold (positive)
            fig_bar = go.Figure(go.Bar(
                x=predictions['Predicted_Return'].values,
                y=predictions['Ticker'].values,
                orientation='h',
                marker=dict(
                    color=predictions['Predicted_Return'].values,
                    colorscale=[[0, '#5B8EDB'], [0.5, '#F2F2F2'], [1, '#C9A227']],
                    showscale=True
                ),
                text=[f"{v:.4f}" for v in predictions['Predicted_Return'].values],
                textposition='auto',
            ))

            fig_bar.update_layout(
                xaxis_title="Rendement Prédit",
                yaxis_title="Action",
                height=500,
                yaxis=dict(autorange="reversed")
            )

            st.plotly_chart(fig_bar, use_container_width=True)

        with col_right:
            st.markdown("#### 🎯 Analyse des Facteurs")

            # Scatter plot if we have momentum data
            if 'Momentum_3M' in predictions.columns and 'Volatility_3M' in predictions.columns:
                fig_scatter = px.scatter(
                    predictions,
                    x='Momentum_3M',
                    y='Predicted_Return',
                    size='Volatility_3M' if 'Volatility_3M' in predictions.columns else None,
                    color='Predicted_Return',
                    hover_data=['Ticker'],
                    color_continuous_scale=[[0, '#5B8EDB'], [0.5, '#F2F2F2'], [1, '#C9A227']],
                    labels={
                        'Momentum_3M': 'Momentum 3 Mois',
                        'Predicted_Return': 'Rendement Prédit',
                        'Volatility_3M': 'Volatilité 3M'
                    }
                )

                fig_scatter.update_layout(height=500)
                st.plotly_chart(fig_scatter, use_container_width=True)
            else:
                st.info("Les données de facteurs (Momentum, Volatilité) ne sont pas disponibles pour l'affichage.")

        # Table détaillée
        st.markdown("---")
        st.markdown("#### 📋 Tableau Détaillé des Prédictions")

        # Format for display
        display_df = predictions.copy()
        if 'Predicted_Return' in display_df.columns:
            display_df['Rendement Prédit (%)'] = display_df['Predicted_Return'].apply(lambda x: f"{x:.4%}")

        st.dataframe(
            display_df,
            use_container_width=True,
            height=400
        )

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

        # Export
        st.markdown("---")
        csv_pred = predictions.to_csv(index=False)
        st.download_button(
            label="📥 Télécharger les Prédictions (CSV)",
            data=csv_pred,
            file_name="ml_predictions.csv",
            mime="text/csv"
        )

        # Warning
        st.warning("""
        ⚠️ **Disclaimer** : Ces prédictions sont basées sur des modèles statistiques et ne constituent pas
        des conseils d'investissement. Les performances passées ne préjugent pas des performances futures.
        """)
