"""
Wafa Gestion - Portfolio Intelligence Platform
MVP Version for Data & AI Internship Challenge 2026
"""

import streamlit as st
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

# Page configuration
# Use absolute path for favicon
favicon_path = str(Path(__file__).parent / "assets" / "wg_icon.jpeg")
st.set_page_config(
    page_title="Wafa Gestion - Portfolio Intelligence",
    page_icon=favicon_path,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Wafa Gestion branding
# Official Wafa Gestion colors:
# Bleu foncé: #003A8F | Doré: #C9A227 | Blanc: #FFFFFF
# Gris foncé: #4D4D4D | Gris clair: #F2F2F2 | Bleu clair: #5B8EDB
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #003A8F;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 3px solid #C9A227;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F2F2F2;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #003A8F;
    }
    .stButton>button {
        background-color: #003A8F;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.5rem 2rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #5B8EDB;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🏦 WAFA GESTION - Portfolio Intelligence Platform</div>', unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state['page'] = "🏠 Accueil"

# Sidebar
with st.sidebar:
    # Use absolute path for logo with padding
    logo_path = Path(__file__).parent / "assets" / "wg_logo.png"
    st.markdown("<div style='padding: 0.5rem 0;'>", unsafe_allow_html=True)
    st.image(str(logo_path), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📊 Navigation")

    # Determine current index based on session state
    pages_list = ["🏠 Accueil", "🔄 Reconstruction", "🔮 Prédictions ML"]
    try:
        current_index = pages_list.index(st.session_state['page'])
    except ValueError:
        current_index = 0
        st.session_state['page'] = "🏠 Accueil"

    # Radio without key to avoid state conflicts
    selected_page = st.radio(
        "Sélectionner une page",
        pages_list,
        index=current_index,
        label_visibility="collapsed"
    )

    # Update session state if selection changed
    if selected_page != st.session_state['page']:
        st.session_state['page'] = selected_page
        st.rerun()

    st.markdown("---")
    st.markdown("### ℹ️ À propos")
    st.info("""
    **Plateforme d'analyse quantitative** pour la reconstruction et l'analyse de portefeuilles OPCVM.

    **Challenge Data & AI 2026**
    """)

# Main content based on selected page (using session state)
if st.session_state['page'] == "🏠 Accueil":
    # Import home page
    from components import home
    home.show()

elif st.session_state['page'] == "🔄 Reconstruction":
    # Import the reconstruction page
    from components import reconstruction
    reconstruction.show()

elif st.session_state['page'] == "🔮 Prédictions ML":
    # Import the predictions page
    from components import predictions
    predictions.show()
