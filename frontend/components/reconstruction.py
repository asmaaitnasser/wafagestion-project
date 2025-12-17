"""
Page 1: Portfolio Reconstruction
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path for utils import
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.import_helper import import_portfolio_reconstructor

# Import backend classes
PortfolioReconstructor = import_portfolio_reconstructor()


def show():
    # Back button
    if st.button("← Retour à l'accueil", key="back_to_home_reconstruction"):
        st.session_state['page'] = "🏠 Accueil"
        st.rerun()

    st.markdown("## 🔄 Reconstruction du Portefeuille WG Actions")

    st.markdown("""
    Cette page permet de **reconstituer** la composition du portefeuille WG Actions
    en utilisant des algorithmes d'optimisation.

    **Objectif** : Minimiser la tracking error entre les rendements réels du fonds
    et les rendements reconstruits à partir des actions individuelles.
    """)

    st.markdown("---")

    # Paramètres
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### ⚙️ Paramètres de Reconstruction")

    with col2:
        st.markdown("### ")

    col_method, col_alpha = st.columns(2)

    with col_method:
        method = st.selectbox(
            "Méthode d'optimisation",
            ["Ridge Regression", "SLSQP (Sequential Least Squares)"],
            help="Ridge: Régularisation L2 pour éviter l'overfitting\nSLSQP: Optimisation avec contraintes"
        )

    with col_alpha:
        if "Ridge" in method:
            alpha = st.slider(
                "Coefficient de régularisation (α)",
                min_value=0.1,
                max_value=10.0,
                value=1.0,
                step=0.1,
                help="Plus α est élevé, plus la régularisation est forte"
            )
        else:
            alpha = None
            st.info("SLSQP n'utilise pas de paramètre α")

    # Bouton reconstruction
    st.markdown("---")

    if st.button("🚀 Lancer la Reconstruction", type="primary", use_container_width=True):

        with st.spinner("⏳ Reconstruction en cours... Cela peut prendre quelques secondes."):
            # Appel au backend
            if "Ridge" in method:
                results = PortfolioReconstructor.reconstruct_ridge(alpha=alpha)
            else:
                results = PortfolioReconstructor.reconstruct_slsqp()

        # Check for errors
        if 'error' in results:
            st.error(f"❌ Erreur lors de la reconstruction: {results['error']}")
            st.stop()

        # Store results in session state
        st.session_state['reconstruction_results'] = results

    # Display results if available
    if 'reconstruction_results' in st.session_state:
        results = st.session_state['reconstruction_results']

        st.success("✅ Reconstruction terminée avec succès !")

        st.markdown("---")
        st.markdown("### 📊 Résultats de la Reconstruction")

        # Metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Tracking Error",
                f"{results['tracking_error']:.4f}",
                help="RMSE entre rendements réels et reconstruits (hebdomadaire)"
            )

        with col2:
            st.metric(
                "R² Score",
                f"{results['r2']:.4f}",
                help="Coefficient de détermination (qualité de l'ajustement)"
            )

        with col3:
            st.metric(
                "Corrélation",
                f"{results['correlation']:.4f}",
                help="Corrélation entre rendements réels et reconstruits"
            )

        with col4:
            nb_actions = len(results['weights'])
            st.metric(
                "Nb Actions",
                nb_actions,
                help="Nombre d'actions dans le portefeuille reconstruit"
            )

        st.markdown("---")

        # Visualisations
        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("#### 📈 Top 10 Pondérations")

            # Bar chart horizontal
            top10 = results['weights'].head(10)
            fig_bar = go.Figure(go.Bar(
                x=top10.values,
                y=top10.index,
                orientation='h',
                marker=dict(color='#003A8F'),
                text=[f"{v:.2%}" for v in top10.values],
                textposition='auto',
            ))

            fig_bar.update_layout(
                xaxis_title="Pondération",
                yaxis_title="Action",
                height=400,
                yaxis=dict(autorange="reversed"),
                showlegend=False
            )

            st.plotly_chart(fig_bar, use_container_width=True)

        with col_right:
            st.markdown("#### 🥧 Répartition du Portefeuille")

            # Pie chart
            top10_pie = results['weights'].head(10)
            other = results['weights'].iloc[10:].sum() if len(results['weights']) > 10 else 0

            if other > 0:
                pie_data = pd.concat([top10_pie, pd.Series({'Autres': other})])
            else:
                pie_data = top10_pie

            # Wafa Gestion color palette for pie chart
            wafa_colors = ['#003A8F', '#5B8EDB', '#C9A227', '#4D4D4D', '#F2F2F2', '#7FA8E5', '#D4AF37', '#6B6B6B', '#E0E0E0', '#A2C4F5']

            fig_pie = go.Figure(data=[go.Pie(
                labels=pie_data.index,
                values=pie_data.values,
                hole=0.3,
                textinfo='label+percent',
                marker=dict(colors=wafa_colors)
            )])

            fig_pie.update_layout(
                height=400,
                showlegend=True,
                legend=dict(orientation="v", x=1.1, y=0.5)
            )

            st.plotly_chart(fig_pie, use_container_width=True)

        # Tracking Performance
        st.markdown("---")
        st.markdown("#### 📉 Performance de Tracking (Rendements Réels vs Reconstruits)")

        timeseries = results['timeseries']

        fig_line = go.Figure()

        fig_line.add_trace(go.Scatter(
            x=timeseries['Date'],
            y=timeseries['WG_RETURN'].cumsum(),
            mode='lines',
            name='Rendement Réel (WG Actions)',
            line=dict(color='#003A8F', width=2)
        ))

        fig_line.add_trace(go.Scatter(
            x=timeseries['Date'],
            y=timeseries['WG_REPL'].cumsum(),
            mode='lines',
            name='Rendement Reconstruit',
            line=dict(color='#C9A227', width=2, dash='dash')
        ))

        fig_line.update_layout(
            xaxis_title="Date",
            yaxis_title="Rendement Cumulé",
            height=400,
            hovermode='x unified',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        st.plotly_chart(fig_line, use_container_width=True)

        # Tableau détaillé
        with st.expander("📋 Voir toutes les pondérations"):
            weights_df = results['weights'].reset_index()
            weights_df.columns = ['Action', 'Pondération']
            weights_df['Pondération (%)'] = weights_df['Pondération'].apply(lambda x: f"{x:.4%}")

            st.dataframe(
                weights_df,
                use_container_width=True,
                height=400
            )

        # Export
        st.markdown("---")
        col_export1, col_export2 = st.columns(2)

        with col_export1:
            # Export weights as CSV
            csv_weights = results['weights'].to_csv()
            st.download_button(
                label="📥 Télécharger les Pondérations (CSV)",
                data=csv_weights,
                file_name="wg_actions_weights.csv",
                mime="text/csv"
            )

        with col_export2:
            # Export timeseries as CSV
            csv_timeseries = timeseries.to_csv(index=False)
            st.download_button(
                label="📥 Télécharger la Série Temporelle (CSV)",
                data=csv_timeseries,
                file_name="wg_actions_tracking.csv",
                mime="text/csv"
            )
