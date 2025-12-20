"""
Wafa Gestion - Portfolio Intelligence Platform
Premium Design Version - Challenge Data & AI 2026
"""

import streamlit as st
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

# Page configuration
favicon_path = str(Path(__file__).parent / "assets" / "wg_icon.jpeg")
st.set_page_config(
    page_title="Wafa Gestion - Portfolio Intelligence",
    page_icon=favicon_path,
    layout="wide",
    initial_sidebar_state="expanded"  # Force sidebar to be open
)

# Load Custom CSS
css_path = Path(__file__).parent / "styles" / "custom.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Additional inline CSS for specific tweaks
st.markdown("""
    <style>
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        padding-top: 2rem;
    }

    /* Sidebar toggle button - make it more visible */
    [data-testid="collapsedControl"] {
        background: linear-gradient(135deg, #003A8F 0%, #5B8EDB 100%) !important;
        border-radius: 0 12px 12px 0 !important;
        padding: 1rem 0.5rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2) !important;
    }

    [data-testid="collapsedControl"]:hover {
        box-shadow: 0 6px 12px -2px rgba(0, 0, 0, 0.3) !important;
        transform: translateX(2px);
    }

    /* Arrow icon in collapsed state */
    [data-testid="collapsedControl"] svg {
        color: white !important;
        width: 24px !important;
        height: 24px !important;
    }

    /* Style navigation buttons */
    [data-testid="stSidebar"] button {
        border-radius: 12px !important;
        padding: 1rem 1.25rem !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        margin-bottom: 0.75rem !important;
        border: none !important;
        outline: none !important;
    }

    [data-testid="stSidebar"] button[kind="secondary"] {
        background: white !important;
        color: #4D4D4D !important;
        box-shadow: 0 0 0 2px #E0E0E0 inset, 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    }

    [data-testid="stSidebar"] button[kind="secondary"]:hover {
        box-shadow: 0 0 0 2px #003A8F inset, 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
        transform: translateX(4px) !important;
    }

    [data-testid="stSidebar"] button[kind="secondary"]:focus {
        box-shadow: 0 0 0 2px #003A8F inset, 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
    }

    [data-testid="stSidebar"] button[kind="primary"] {
        background: linear-gradient(135deg, #003A8F 0%, #5B8EDB 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
        transform: translateX(4px) !important;
    }

    [data-testid="stSidebar"] button[kind="primary"]:hover {
        box-shadow: 0 6px 12px -2px rgba(0, 0, 0, 0.15) !important;
        transform: translateX(6px) !important;
    }

    [data-testid="stSidebar"] button[kind="primary"]:focus {
        box-shadow: 0 6px 12px -2px rgba(0, 0, 0, 0.15) !important;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #F2F2F2;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #003A8F 0%, #5B8EDB 100%);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #003A8F;
    }

    /* Smooth transitions for all elements */
    * {
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Hover effect for navigation buttons */
    [data-testid="stSidebar"] div[style*="cursor: pointer"]:hover {
        transform: translateX(6px) !important;
        box-shadow: 0 6px 12px -2px rgba(0, 0, 0, 0.15) !important;
    }

    /* Force sidebar to stay open with proper width */
    section[data-testid="stSidebar"] {
        width: 21rem !important;
        min-width: 21rem !important;
        max-width: 21rem !important;
    }

    section[data-testid="stSidebar"] > div {
        width: 21rem !important;
    }

    /* Ensure sidebar is visible when collapsed */
    section[data-testid="stSidebar"][aria-expanded="false"] {
        margin-left: 0 !important;
    }
    </style>
    <script>
    // Force sidebar to stay open on page load
    window.addEventListener('load', function() {
        const sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
        if (sidebar) {
            sidebar.setAttribute('aria-expanded', 'true');
        }
    });
    </script>
""", unsafe_allow_html=True)

# Enhanced Premium Header with advanced animations
st.markdown("""
    <div class="main-header animate-fadeIn" style='
        background: linear-gradient(135deg, #003A8F 0%, #5B8EDB 50%, #7FA8E5 100%);
        background-size: 200% 200%;
        animation: gradient-shift 10s ease infinite;
        position: relative;
        overflow: hidden;
    '>
        <div style='position: relative; z-index: 1;'>
            <h1 style='
                font-size: 2.75rem;
                font-weight: 900;
                margin-bottom: 0.5rem;
                text-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
                letter-spacing: -0.02em;
            '>🏦 WAFA GESTION</h1>
            <p style='
                font-size: 1.2rem;
                opacity: 0.95;
                font-weight: 500;
                margin: 0;
            '>Portfolio Intelligence Platform • Challenge Data & AI 2026</p>
        </div>
        <!-- Animated background decoration -->
        <div style='
            position: absolute;
            top: -50%;
            right: -10%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
            border-radius: 50%;
            animation: pulse 6s ease-in-out infinite;
        '></div>
        <div style='
            position: absolute;
            bottom: -30%;
            left: -5%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(201, 162, 39, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            animation: pulse 8s ease-in-out infinite;
            animation-delay: 2s;
        '></div>
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state['page'] = "🏠 Accueil"

# Premium Sidebar
with st.sidebar:
    # Logo in white card at the top
    logo_path = Path(__file__).parent / "assets" / "wg_logo.png"
    if logo_path.exists():
        # Use HTML img tag inside the div to keep it contained
        import base64
        with open(logo_path, "rb") as f:
            logo_data = base64.b64encode(f.read()).decode()

        st.markdown(f"""
            <div style='
                background: white;
                border-radius: 16px;
                padding: 2rem 1.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                margin-bottom: 2rem;
                text-align: center;
            '>
                <img src="data:image/png;base64,{logo_data}" style="width: 100%; max-width: 300px;">
            </div>
        """, unsafe_allow_html=True)

    # Navigation Title
    st.markdown("""
        <div style='
            font-size: 0.75rem;
            font-weight: 700;
            color: #4D4D4D;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        '>
            Navigation
        </div>
    """, unsafe_allow_html=True)

    # Custom Navigation Buttons
    pages = [
        {"id": "🏠 Accueil", "icon": "🏠", "label": "Accueil"},
        {"id": "🔄 Reconstruction", "icon": "🔄", "label": "Reconstruction"},
        {"id": "🔮 Prédictions ML", "icon": "🔮", "label": "Prédictions ML"}
    ]

    for page in pages:
        is_active = st.session_state['page'] == page['id']

        # Button styling based on active state
        if is_active:
            button_label = f"**{page['icon']} {page['label']}**"
            button_type = "primary"
        else:
            button_label = f"{page['icon']} {page['label']}"
            button_type = "secondary"

        # Create clickable button
        if st.button(
            button_label,
            key=f"nav_{page['id']}",
            use_container_width=True,
            type=button_type
        ):
            st.session_state['page'] = page['id']
            st.rerun()

    # Divider
    st.markdown("""
        <div style='
            height: 2px;
            background: linear-gradient(90deg, #003A8F 0%, #C9A227 100%);
            margin: 2rem 0;
            border-radius: 2px;
        '></div>
    """, unsafe_allow_html=True)

    # About section
    st.markdown("""
        <div style='
            background: linear-gradient(135deg, #003A8F 0%, #5B8EDB 100%);
            border-radius: 16px;
            padding: 1.5rem;
            color: white;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        '>
            <div style='font-weight: 700; font-size: 1rem; margin-bottom: 0.75rem;'>
                ℹ️ À propos
            </div>
            <p style='font-size: 0.875rem; line-height: 1.6; margin: 0; opacity: 0.95;'>
                <strong>Plateforme d'analyse quantitative</strong> pour la reconstruction
                et l'optimisation de portefeuilles OPCVM.
            </p>
            <div style='
                margin-top: 1rem;
                padding-top: 1rem;
                border-top: 1px solid rgba(255,255,255,0.2);
                font-size: 0.8rem;
                opacity: 0.9;
            '>
                <strong>Challenge Data & AI 2026</strong><br>
                Wafa Gestion
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Tech stack
    st.markdown("""
        <div style='margin-top: 1.5rem; padding: 1rem; background: white; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);'>
            <div style='font-size: 0.7rem; font-weight: 700; color: #4D4D4D; margin-bottom: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em;'>
                Tech Stack
            </div>
            <div style='display: flex; flex-wrap: wrap; gap: 0.5rem;'>
                <span class='badge badge-info' style='font-size: 0.75rem;'>Python</span>
                <span class='badge badge-info' style='font-size: 0.75rem;'>Streamlit</span>
                <span class='badge badge-info' style='font-size: 0.75rem;'>ML</span>
                <span class='badge badge-info' style='font-size: 0.75rem;'>Plotly</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main content routing
if st.session_state['page'] == "🏠 Accueil":
    from components import home
    home.show()

elif st.session_state['page'] == "🔄 Reconstruction":
    from components import reconstruction
    reconstruction.show()

elif st.session_state['page'] == "🔮 Prédictions ML":
    from components import predictions
    predictions.show()

# Footer
st.markdown("""
    <div style='
        margin-top: 4rem;
        padding: 2rem;
        text-align: center;
        color: #4D4D4D;
        font-size: 0.875rem;
        border-top: 2px solid #F2F2F2;
    '>
        <div style='margin-bottom: 0.5rem; font-weight: 600;'>
            Wafa Gestion - Portfolio Intelligence Platform
        </div>
        <div style='opacity: 0.7;'>
            Challenge Data & AI Internship 2026 • Powered by Machine Learning & Optimization
        </div>
    </div>
""", unsafe_allow_html=True)
