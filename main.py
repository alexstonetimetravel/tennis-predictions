"""
Hlavná Streamlit aplikácia pre analýzu a predikciu tenisových zápasov
"""
import streamlit as st
import os
import logging

# Import stránok
from pages.dashboard import show_dashboard
from pages.predictions import show_predictions
from pages.simulator import show_simulator
from pages.calibration import show_calibration

# Konfigurácia logovania
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Konfigurácia stránky
st.set_page_config(
    page_title="🎾 Tenisová Analýza & Predikcie",
    page_icon="🎾",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Hlavná funkcia aplikácie"""
    
    # Sidebar navigácia
    st.sidebar.title("🎾 Tenisová Analýza")
    st.sidebar.markdown("---")
    
    menu_options = {
        "📺 Dashboard": "dashboard",
        "🔮 Predikcie": "predictions", 
        "⏪ Historický simulátor": "simulator",
        "⚙️ Kalibrácia modelu": "calibration"
    }
    
    selected_page = st.sidebar.selectbox(
        "Navigácia",
        options=list(menu_options.keys()),
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ O aplikácii")
    st.sidebar.markdown("""
    **Tenisová Analýza & Predikcie** je komplexná aplikácia pre:
    
    - 📊 Sledovanie live zápasov
    - 🤖 ML predikcie výsledkov
    - 📈 ELO rating systém
    - 🔬 Historické simulácie
    - ⚙️ Automatická kalibrácia
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔑 API Status")
    
    sportdevs_key = os.getenv("SPORTDEVS_API_KEY", "")
    freewebapi_key = os.getenv("FREEWEBAPI_KEY", "")
    
    if sportdevs_key:
        st.sidebar.success("✅ SportDevs API")
    else:
        st.sidebar.warning("⚠️ SportDevs API kľúč chýba")
    
    if freewebapi_key:
        st.sidebar.success("✅ FreeWebApi")
    else:
        st.sidebar.warning("⚠️ FreeWebApi kľúč chýba")
    
    if not sportdevs_key and not freewebapi_key:
        st.sidebar.error("❌ Žiadne API klúče - použije sa web scraping")
    
    page_key = menu_options[selected_page]
    
    try:
        if page_key == "dashboard":
            show_dashboard()
        elif page_key == "predictions":
            show_predictions()
        elif page_key == "simulator":
            show_simulator()
        elif page_key == "calibration":
            show_calibration()
        else:
            st.error("Neznáma stránka")
            
    except Exception as e:
        st.error(f"Chyba pri načítaní stránky: {e}")
        logger.error(f"Chyba v aplikácii: {e}")
        
        if st.checkbox("Zobraziť debug informácie"):
            st.exception(e)
    
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            "<div style='text-align: center; color: #666;'>"
            "🎾 Tenisová Analýza & Predikcie | "
            "Vyvinuté s ❤️ pomocou Streamlit"
            "</div>",
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
