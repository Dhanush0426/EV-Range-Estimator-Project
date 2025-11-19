import streamlit as st
import pandas as pd
import joblib
import re
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="⚡ EV Range Predictor",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown(
    """
<style>
    .main { padding-top: 2rem; }
    .stTitle { color: #2E7D32; font-size: 2.5rem !important; }
    .metric-card {
        background: linear-gradient(135deg, #2E7D32, #66BB6A);
        color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton > button { 
        width: 100%;
        background: #2E7D32;
        color: white;
        font-weight: bold;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Load model
model = joblib.load("ev_range_model.pkl")

# Sidebar
st.sidebar.title("⚡ Navigation")
page = st.sidebar.radio(
    "Choose a section:", ["Home", "Range Predictor", "Chatbot", "About"]
)


# ---------------- HOME ----------------
if page == "Home":
    st.title("⚡ Electric Vehicle Range Predictor")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            '<div class="metric-card"><h3>🔋</h3><p>Battery Aware</p></div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            '<div class="metric-card"><h3>⚡</h3><p>ML Powered</p></div>',
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            '<div class="metric-card"><h3>💬</h3><p>AI Chat</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("📌 How It Works")

    with st.expander("🔋 Range Predictor", expanded=True):
        st.write(
            """
        Input your EV specifications:
        - **Battery Capacity (kWh)** - Total battery size
        - **Efficiency (Wh/km)** - Energy consumption rate
        - **Top Speed (km/h)** - Maximum speed
        
        Our ML model calculates estimated driving range instantly!
        """
        )

    with st.expander("💬 EV Chatbot"):
        st.write(
            """
        Ask anything about electric vehicles:
        - Battery health & lifespan
        - Charging best practices
        - Range optimization tips
        - EV specifications & comparisons
        """
        )


# ---------------- RANGE PREDICTOR ----------------
elif page == "Range Predictor":
    st.title("🔋 EV Range Predictor")
    st.write("Enter your EV specs and get instant range prediction")

    # Input method selection
    input_method = st.radio(
        "📝 Input Method:", ["Sliders", "Number Boxes"], horizontal=True
    )

    if input_method == "Sliders":
        col1, col2, col3 = st.columns(3)
        with col1:
            battery = st.slider("🔋 Battery (kWh)", 10.0, 150.0, 60.0, step=1.0)
        with col2:
            efficiency = st.slider(
                "⚡ Efficiency (Wh/km)", 100.0, 300.0, 150.0, step=5.0
            )
        with col3:
            speed = st.slider("🏎️ Top Speed (km/h)", 60.0, 300.0, 180.0, step=10.0)
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            battery = st.number_input("🔋 Battery (kWh)", 10.0, 150.0, 60.0, step=1.0)
        with col2:
            efficiency = st.number_input(
                "⚡ Efficiency (Wh/km)", 100.0, 300.0, 150.0, step=5.0
            )
        with col3:
            speed = st.number_input("🏎️ Top Speed (km/h)", 60.0, 300.0, 180.0, step=10.0)

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚗 Predict Range", use_container_width=True):
            df = pd.DataFrame(
                [[battery, efficiency, speed]],
                columns=[
                    "battery_capacity_kWh",
                    "efficiency_wh_per_km",
                    "top_speed_kmh",
                ],
            )
            result = model.predict(df)[0]

            # Display result with visual indicator
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Estimated Range", f"{result:.1f} km", delta="🎯")
            with col_b:
                st.metric("Hours (50km/h avg)", f"{result/50:.1f} hrs", delta="⏱️")

    # Info box
    st.info(
        """
    💡 **Tips to Increase Range:**
    - Maintain proper tire pressure
    - Avoid rapid acceleration
    - Remove unnecessary weight
    - Optimize charging habits
    """
    )


# ------------------- CHATBOT (Gemini API) -------------------
elif page == "Chatbot":
    st.title("🤖 EV Chatbot (Gemini AI)")
    st.write("Your intelligent EV assistant - ask anything!")

    import os
    import google.generativeai as genai

    # Load API key
    from dotenv import load_dotenv

    load_dotenv()
    GEMINI_KEY = os.getenv("GEMINI_API_KEY")

    if not GEMINI_KEY:
        st.error("❌ Gemini API key not found in .env file")
        st.stop()

    # Configure Gemini
    genai.configure(api_key=GEMINI_KEY)

    # Define model (using latest Gemini 2.5 Pro for best performance)
    model_g = genai.GenerativeModel("gemini-2.5-pro")

    # ----------------------- FAQ Section -----------------------
    st.subheader("📘 Quick Tips")

    col1, col2 = st.columns(2)
    with col1:
        with st.expander("❓ How to increase range?"):
            st.write(
                "✅ Maintain tire pressure\n✅ Avoid high speeds\n✅ Remove extra weight\n✅ Drive smoothly"
            )

    with col2:
        with st.expander("❓ Does fast charging damage battery?"):
            st.write(
                "⚠️ Yes, regular DC fast charging can increase battery wear due to heat generation."
            )

    col1, col2 = st.columns(2)
    with col1:
        with st.expander("❓ What is Wh/km?"):
            st.write("Energy consumption rate. Lower = better efficiency! 🎯")

    with col2:
        with st.expander("❓ How is range calculated?"):
            st.write("Range = Battery (kWh) ÷ Efficiency (kWh/km)")

    st.markdown("---")

    # ------------------- ML-Based Range Prediction (NLP) -------------------
    import re
    import pandas as pd

    def extract_specs(msg):
        b = re.search(r"(\d+(\.\d+)?)\s*kwh", msg, re.I)
        e = re.search(r"(\d+(\.\d+)?)\s*wh", msg, re.I)
        s = re.search(r"(\d+(\.\d+)?)\s*km/h", msg, re.I)

        return (
            float(b.group(1)) if b else None,
            float(e.group(1)) if e else None,
            float(s.group(1)) if s else None,
        )

    def ml_range_prediction(text):
        battery, eff, speed = extract_specs(text)
        if battery and eff and speed:
            df = pd.DataFrame(
                [[battery, eff, speed]],
                columns=[
                    "battery_capacity_kWh",
                    "efficiency_wh_per_km",
                    "top_speed_kmh",
                ],
            )
            pred = model.predict(df)[0]
            return f"⚡ Estimated EV Range: **{pred:.2f} km**"
        return None

    # ----------------------- USER INPUT -----------------------
    user_msg = st.text_area(
        "💬 Ask your EV question:",
        placeholder="e.g., 'How to maximize my EV range?' or 'Does temperature affect battery?'",
        height=80,
    )

    if user_msg:
        col1, col2 = st.columns([1, 1])

        with col1:
            # 1. Check if input has numerical specs → ML prediction
            ml_answer = ml_range_prediction(user_msg)
            if ml_answer:
                st.success(ml_answer)

        with col2:
            # 2. Ask Gemini for answer
            with st.spinner("💡 Thinking..."):
                try:
                    response = model_g.generate_content(user_msg)
                    if response and response.text:
                        st.info(response.text)
                    else:
                        st.warning("⚠️ No response received from Gemini API")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")


# ---------------- ABOUT ----------------
elif page == "About":
    st.title("ℹ️ About This App")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Features")
        st.write(
            """
        ✨ **Smart Range Prediction** - ML-powered accuracy
        
        🤖 **AI Chatbot** - Powered by Gemini 2.5 Pro
        
        💾 **Instant Calculations** - Real-time predictions
        
        🎨 **Clean UI** - Simple & intuitive design
        """
        )

    with col2:
        st.subheader("🛠️ Technologies")
        st.write(
            """
        🐍 **Python** - Core language
        
        📚 **Streamlit** - Web framework
        
        🤖 **Google Gemini** - AI Assistant
        
        🧠 **Random Forest** - ML Model
        """
        )

    st.markdown("---")
    st.write("**Developed by:** Dhanush M Aradhyamath | **Project:** AICTE Internship")
