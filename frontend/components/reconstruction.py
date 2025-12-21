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
    # Enhanced Header Section
    st.markdown("""
        <div class="gradient-card animate-fadeIn" style='
            padding: 2.5rem;
            margin-bottom: 2rem;
            border-radius: 20px;
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
                '>🔄</div>
                <div>
                    <h1 style='color: white; margin: 0; font-size: 2.5rem; font-weight: 800;'>
                        Reconstruction du Portefeuille
                    </h1>
                    <p style='color: rgba(255, 255, 255, 0.9); margin: 0.5rem 0 0 0; font-size: 1.1rem;'>
                        WG Actions - Analyse Quantitative
                    </p>
                </div>
            </div>
            <p style='color: rgba(255, 255, 255, 0.95); font-size: 1rem; line-height: 1.6; margin-top: 1rem;'>
                Reconstituer la composition du portefeuille WG Actions en minimisant la tracking error 
                entre les rendements réels et reconstruits grâce à des algorithmes d'optimisation avancés.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Back button with enhanced styling
    if st.button("← Retour à l'accueil", key="back_to_home_reconstruction", use_container_width=False):
        st.session_state['page'] = "🏠 Accueil"
        st.rerun()

    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    # Enhanced Parameters Section
    st.markdown("""
        <div class="custom-card animate-slideUp" style='margin-bottom: 2rem;'>
            <h2 style='color: #003A8F; font-size: 1.75rem; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.75rem;'>
                <span style='font-size: 2rem;'>⚙️</span>
                Paramètres de Reconstruction
            </h2>
    """, unsafe_allow_html=True)

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

    st.markdown("</div>", unsafe_allow_html=True)

    # Enhanced Action Button
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
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
                        <h3 style='margin: 0; font-size: 1.5rem;'>Reconstruction terminée avec succès !</h3>
                        <p style='margin: 0.5rem 0 0 0; opacity: 0.95;'>Les résultats sont disponibles ci-dessous</p>
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
                    <span style='font-size: 2.5rem;'>📊</span>
                    Résultats de la Reconstruction
                </h2>
        """, unsafe_allow_html=True)

        # Enhanced Metrics Display
        col1, col2, col3, col4 = st.columns(4)

        metrics_info = [
            {
                "label": "Tracking Error",
                "value": f"{results['tracking_error']:.4f}",
                "color": "#10B981" if results['tracking_error'] < 0.015 else "#F59E0B",
                "icon": "📉"
            },
            {
                "label": "R² Score",
                "value": f"{results['r2']:.4f}",
                "color": "#10B981" if results['r2'] > 0.8 else "#F59E0B",
                "icon": "🎯"
            },
            {
                "label": "Corrélation",
                "value": f"{results['correlation']:.4f}",
                "color": "#10B981" if results['correlation'] > 0.9 else "#F59E0B",
                "icon": "📈"
            },
            {
                "label": "Nb Actions",
                "value": len(results['weights']),
                "color": "#003A8F",
                "icon": "📊"
            }
        ]

        for idx, (col, metric) in enumerate(zip([col1, col2, col3, col4], metrics_info)):
            with col:
                st.markdown(f"""
                    <div class="metric-card animate-slideUp" style='animation-delay: {idx * 0.1}s;'>
                        <div style='font-size: 1.5rem; margin-bottom: 0.5rem;'>{metric['icon']}</div>
                        <div class="metric-label">{metric['label']}</div>
                        <div class="metric-value" style='color: {metric['color']};'>{metric['value']}</div>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

        # Enhanced Visualizations
        st.markdown("""
            <div style='
                background: white;
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
            '>
                <h2 style='color: #003A8F; font-size: 1.75rem; margin-bottom: 1.5rem;'>
                    📊 Visualisations
                </h2>
        """, unsafe_allow_html=True)

        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("#### 📈 Top 10 Pondérations")

            # Enhanced Bar chart with gradient
            top10 = results['weights'].head(10)
            fig_bar = go.Figure(go.Bar(
                x=top10.values,
                y=top10.index,
                orientation='h',
                marker=dict(
                    color=top10.values,
                    colorscale=[[0, '#5B8EDB'], [0.5, '#003A8F'], [1, '#C9A227']],
                    showscale=True,
                    colorbar=dict(title=dict(text="Pondération", font=dict(color='#003A8F', family='Inter')))
                ),
                text=[f"{v:.2%}" for v in top10.values],
                textposition='auto',
                textfont=dict(color='white', size=12, family='Inter'),
                hovertemplate='<b>%{y}</b><br>Pondération: %{x:.2%}<extra></extra>'
            ))

            fig_bar.update_layout(
                xaxis_title="Pondération",
                yaxis_title="Action",
                height=450,
                yaxis=dict(autorange="reversed"),
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#4D4D4D'),
                margin=dict(l=20, r=20, t=20, b=20)
            )

            st.plotly_chart(fig_bar, use_container_width=True)

        with col_right:
            st.markdown("#### 🥧 Répartition du Portefeuille")

            # Enhanced Pie chart with better styling
            top10_pie = results['weights'].head(10)
            other = results['weights'].iloc[10:].sum() if len(results['weights']) > 10 else 0

            if other > 0:
                pie_data = pd.concat([top10_pie, pd.Series({'Autres': other})])
            else:
                pie_data = top10_pie

            # Enhanced Wafa Gestion color palette
            wafa_colors = ['#003A8F', '#5B8EDB', '#C9A227', '#10B981', '#F59E0B', '#7FA8E5', '#D4AF37', '#34D399', '#FBBF24', '#A2C4F5']

            fig_pie = go.Figure(data=[go.Pie(
                labels=pie_data.index,
                values=pie_data.values,
                hole=0.4,
                textinfo='label+percent',
                textposition='outside',
                marker=dict(
                    colors=wafa_colors[:len(pie_data)],
                    line=dict(color='white', width=2)
                ),
                hovertemplate='<b>%{label}</b><br>Pondération: %{percent}<br>Valeur: %{value:.4f}<extra></extra>'
            )])

            fig_pie.update_layout(
                height=450,
                showlegend=True,
                legend=dict(
                    orientation="v", 
                    x=1.15, 
                    y=0.5,
                    font=dict(family='Inter', color='#4D4D4D', size=11)
                ),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family='Inter', color='#4D4D4D', size=12),
                margin=dict(l=20, r=20, t=20, b=20)
            )

            st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # Enhanced Tracking Performance Chart
        st.markdown("""
            <div style='
                background: white;
                padding: 2rem;
                border-radius: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
            '>
                <h2 style='color: #003A8F; font-size: 1.75rem; margin-bottom: 1.5rem;'>
                    📉 Performance de Tracking
                </h2>
                <p style='color: #4D4D4D; margin-bottom: 1.5rem;'>
                    Comparaison des rendements réels vs reconstruits (cumulés)
                </p>
        """, unsafe_allow_html=True)

        timeseries = results['timeseries']

        fig_line = go.Figure()

        fig_line.add_trace(go.Scatter(
            x=timeseries['Date'],
            y=timeseries['WG_RETURN'].cumsum(),
            mode='lines',
            name='Rendement Réel (WG Actions)',
            line=dict(color='#003A8F', width=3),
            fill='tozeroy',
            fillcolor='rgba(0, 58, 143, 0.1)',
            hovertemplate='<b>Réel</b><br>Date: %{x}<br>Rendement: %{y:.4f}<extra></extra>'
        ))

        fig_line.add_trace(go.Scatter(
            x=timeseries['Date'],
            y=timeseries['WG_REPL'].cumsum(),
            mode='lines',
            name='Rendement Reconstruit',
            line=dict(color='#C9A227', width=3, dash='dash'),
            fill='tozeroy',
            fillcolor='rgba(201, 162, 39, 0.1)',
            hovertemplate='<b>Reconstruit</b><br>Date: %{x}<br>Rendement: %{y:.4f}<extra></extra>'
        ))

        fig_line.update_layout(
            xaxis_title="Date",
            yaxis_title="Rendement Cumulé",
            height=450,
            hovermode='x unified',
            legend=dict(
                orientation="h", 
                yanchor="bottom", 
                y=1.02, 
                xanchor="right", 
                x=1,
                font=dict(family='Inter', color='#4D4D4D', size=12)
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Inter', color='#4D4D4D'),
            margin=dict(l=20, r=20, t=40, b=20),
            xaxis=dict(
                gridcolor='rgba(0, 0, 0, 0.05)',
                showgrid=True
            ),
            yaxis=dict(
                gridcolor='rgba(0, 0, 0, 0.05)',
                showgrid=True
            )
        )

        st.plotly_chart(fig_line, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

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
