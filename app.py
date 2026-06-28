import streamlit as st
import pickle, numpy as np, pandas as pd
from config import PAGE_CONFIG, MODEL_PATH
from styles import get_css
from utils import get_aqi_category, get_health_tips, get_aqi_color, get_aqi_emoji
from components import render_header, render_result, render_tips, render_placeholder, render_aqi_scale_card, render_stats, render_footer

st.set_page_config(**PAGE_CONFIG)
st.markdown(get_css(), unsafe_allow_html=True)

@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

model = load_model()
render_header()

st.markdown('<div class="page-wrap">', unsafe_allow_html=True)

left, right = st.columns([1.22, 1], gap="large")

with left:
    st.markdown("""
    <div class="panel">
        <div class="panel-eyebrow">Step 1 — Input Data</div>
        <div class="panel-heading">Pollutant Concentrations</div>
        <div class="panel-sub">All values in µg/m³ unless noted. Defaults set to 0.</div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("aqi_form"):

        st.markdown('<div class="group-label">Particulate Matter</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            pm25 = st.number_input("PM2.5", min_value=0.0, max_value=1000.0, value=0.0, step=0.1, format="%.2f")
        with c2:
            pm10 = st.number_input("PM10",  min_value=0.0, max_value=1500.0, value=0.0, step=0.1, format="%.2f")

        st.markdown('<div class="group-label">Nitrogen Compounds</div>', unsafe_allow_html=True)
        c3, c4, c5 = st.columns(3)
        with c3:
            no  = st.number_input("NO",  min_value=0.0, max_value=400.0, value=0.0, step=0.1, format="%.2f")
        with c4:
            no2 = st.number_input("NO₂", min_value=0.0, max_value=400.0, value=0.0, step=0.1, format="%.2f")
        with c5:
            nox = st.number_input("NOx", min_value=0.0, max_value=500.0, value=0.0, step=0.1, format="%.2f")

        st.markdown('<div class="group-label">Other Pollutants</div>', unsafe_allow_html=True)
        c6, c7, c8, c9 = st.columns(4)
        with c6:
            nh3 = st.number_input("NH₃",       min_value=0.0, max_value=400.0, value=0.0, step=0.1,  format="%.2f")
        with c7:
            co  = st.number_input("CO (mg/m³)", min_value=0.0, max_value=200.0, value=0.0, step=0.01, format="%.2f")
        with c8:
            so2 = st.number_input("SO₂",        min_value=0.0, max_value=200.0, value=0.0, step=0.1,  format="%.2f")
        with c9:
            o3  = st.number_input("O₃",         min_value=0.0, max_value=300.0, value=0.0, step=0.1,  format="%.2f")

        st.markdown('<div class="group-label">Volatile Organic Compounds</div>', unsafe_allow_html=True)
        c10, c11, c12 = st.columns(3)
        with c10:
            benzene = st.number_input("Benzene", min_value=0.0, max_value=500.0, value=0.0, step=0.01, format="%.2f")
        with c11:
            toluene = st.number_input("Toluene", min_value=0.0, max_value=500.0, value=0.0, step=0.01, format="%.2f")
        with c12:
            xylene  = st.number_input("Xylene",  min_value=0.0, max_value=200.0, value=0.0, step=0.01, format="%.2f")

        submitted = st.form_submit_button("⚡  Predict Air Quality Index", use_container_width=True)

with right:
    if submitted:
        all_values = [pm25, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene]
        if all(v == 0.0 for v in all_values):
            render_aqi_scale_card()
            st.warning("⚠️ All values are zero. Please enter at least one pollutant concentration before predicting.")
        else:
            # ✅ Fix 2 — DataFrame with feature names prevents sklearn warning
            input_df = pd.DataFrame({
                "PM2.5":   [pm25],
                "PM10":    [pm10],
                "NO":      [no],
                "NO2":     [no2],
                "NOx":     [nox],
                "NH3":     [nh3],
                "CO":      [co],
                "SO2":     [so2],
                "O3":      [o3],
                "Benzene": [benzene],
                "Toluene": [toluene],
                "Xylene":  [xylene],
            })
            aqi_value = float(model.predict(input_df)[0])
            category, desc = get_aqi_category(aqi_value)
            color = get_aqi_color(category)
            emoji = get_aqi_emoji(category)
            tips  = get_health_tips(category)
            render_result(aqi_value, category, desc, color, emoji)
            render_tips(tips, color)
            render_aqi_scale_card()
    else:
        render_placeholder()

render_stats()
st.markdown('</div>', unsafe_allow_html=True)
render_footer()