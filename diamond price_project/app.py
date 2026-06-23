
import streamlit as st
import joblib
import numpy as np

# Page Settings
st.set_page_config(
    page_title="Diamond Price Predictor",
    page_icon="💎",
    layout="centered"
)

# Custom Design
st.markdown("""
<style>

/* 🌟 Warm Gold Background */
.stApp {
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    color: #2b2b2b;
}

/* Text */
p, div, span, label {
    color: #2b2b2b !important;
}

/* Title */
.title{
    text-align:center;
    color:#5a3e2b;
    font-size:50px;
    font-weight:bold;
    margin-bottom:20px;
}

/* Headings */
h1, h2, h3 {
    color: #8b5e3c !important;
}

/* Result Box */
.result{
    background: linear-gradient(90deg, #ffe259, #ffa751);
    color: #2b2b2b;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
    margin-top:20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
}

/* Button */
.stButton>button {
    background-color: #c19a6b;
    color: white;
    font-weight: bold;
    border-radius: 10px;
}

.stButton>button:hover {
    background-color: #a67c52;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Load Model
import joblib

MODEL_PATH = r"C:\Users\USER\Desktop\krishna priya\diamond price_project\diamond_price_model.pkl"
model = joblib.load(MODEL_PATH)

# Title
st.markdown(
    '<div class="title">💎 Diamond Price Prediction System</div>',
    unsafe_allow_html=True
)

st.write("### Enter Diamond Details")

# Input Card
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    carat = st.number_input("💎 Carat", min_value=0.0)

with col2:
    depth = st.number_input("📏 Depth", min_value=0.0)

with col3:
    table = st.number_input("📊 Table", min_value=0.0)

col4, col5, col6 = st.columns(3)

with col4:
    x = st.number_input("↔ Length (X)", min_value=0.0)

with col5:
    y = st.number_input("↕ Width (Y)", min_value=0.0)

with col6:
    z = st.number_input("⬆ Height (Z)", min_value=0.0)

st.markdown("</div>", unsafe_allow_html=True)

# Prediction
if st.button("🚀 Predict Price", use_container_width=True):

    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go

    # =========================
    # PREDICTION
    # =========================
    input_data = np.array([[carat, depth, table, x, y, z]])
    result = model.predict(input_data)[0]

   # st.balloons()

    st.markdown(f"""
        <div class="result">
            💰 Estimated Diamond Price <br>
            ${result:,.2f}
        </div>
    """, unsafe_allow_html=True)

    # =========================
    # CONFIDENCE
    # =========================
    confidence = min(0.95, max(0.60, 0.65 + (carat * 0.1)))

    st.subheader("🎯 Prediction Confidence")
    st.progress(int(confidence * 100))
    st.write(f"Confidence: {confidence*100:.1f}%")

    # =========================
    # CATEGORY
    # =========================
    st.subheader("📌 Diamond Category")

    if result < 2000:
        st.success("💠 Budget Diamond")
    elif result < 8000:
        st.info("💎 Mid Range Diamond")
    else:
        st.warning("💍 Luxury Diamond")

    # =========================
    # FEATURES
    # =========================
    features = ["Carat", "Depth", "Table", "X", "Y", "Z"]
    values = [carat, depth, table, x, y, z]

    # =========================
    # BAR CHART
    # =========================
    st.subheader("📊 Feature Bar Chart")
    df = pd.DataFrame({"Feature": features, "Value": values})
    fig = px.bar(df, x="Feature", y="Value", color="Value", text="Value")
    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # RADAR
    # =========================
    st.subheader("📡 Radar View")
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(r=values, theta=features, fill='toself'))
    st.plotly_chart(fig_radar, use_container_width=True)

    # =========================
    # AI INSIGHT
    # =========================
    st.subheader("🧠 AI Insight")

    if carat > 1:
        st.write("💎 High carat increases price strongly")
    else:
        st.write("💠 Low carat keeps price lower")

    # =========================
    # MARKET
    # =========================
    avg_price = 3932

    st.subheader("📊 Market Comparison")
    st.write(f"Your Price: ${result:,.2f}")
    st.write(f"Market Average: ${avg_price:,.2f}")

    # =========================
    # REVIEW
    # =========================
    st.subheader("⭐ Review")

    if result < 2000:
        st.warning("⭐ 2.5 / 5")
    elif result < 8000:
        st.info("⭐ 4.0 / 5")
    else:
        st.success("⭐ 4.8 / 5")

    # =========================
    # QUALITY SCORE
    # =========================
    st.subheader("🏆 Diamond Quality Score")

    quality_score = (
        min(carat * 30, 30) +
        min(depth / 70 * 20, 20) +
        min(table / 70 * 20, 20) +
        min((x + y + z) * 2, 30)
    )

    st.metric("Quality Score", f"{quality_score:.0f}/100")

    # =========================
    # PRICE RANGE
    # =========================
    st.subheader("💰 Price Range")

    low_price = result * 0.9
    high_price = result * 1.1

    st.write(f"Min Price: ${low_price:,.2f}")
    st.write(f"Max Price: ${high_price:,.2f}")

    # =========================
    # DOWNLOAD REPORT
    # =========================
    st.subheader("📄 Download Report")

    report = f"""
Diamond Report

Carat: {carat}
Depth: {depth}
Table: {table}
X: {x}
Y: {y}
Z: {z}

Price: ${result:,.2f}
Confidence: {confidence*100:.1f}%
"""

    st.download_button(
        "Download Report",
        report,
        file_name="diamond_report.txt"
    )

    # =========================
    # INVESTMENT
    # =========================
    st.subheader("📈 Investment")

    if result > 8000 and carat > 1:
        st.success("💍 Strong investment")
    elif result > 3000:
        st.info("💎 Good value")
    else:
        st.warning("💠 Budget diamond")
    # =========================
# ABOUT PROJECT
# =========================
with st.expander("ℹ About This Project"):
    st.write("""
    This Diamond Price Prediction System uses Machine Learning
    to estimate diamond prices based on:

    ✔ Carat
    ✔ Depth
    ✔ Table
    ✔ Length (X)
    ✔ Width (Y)
    ✔ Height (Z)

    Model: Random Forest Regressor
    Framework: Streamlit
    Visualization: Plotly
    """)

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown(
    """
    <center>
    💎 Diamond Price Prediction System <br>
    Developed by Krishna Priya using Machine Learning & Streamlit
    </center>
    """,
    unsafe_allow_html=True
)