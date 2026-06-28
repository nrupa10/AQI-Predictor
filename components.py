import streamlit as st
import plotly.graph_objects as go

AQI_SCALE = [
    ("#16a34a", "0–50",   "Good",        "Air quality is satisfactory."),
    ("#84cc16", "51–100", "Satisfactory", "Acceptable for most people."),
    ("#f59e0b", "101–200","Moderate",     "Sensitive groups may be affected."),
    ("#ef4444", "201–300","Poor",         "Health effects for everyone."),
    ("#a855f7", "301–400","Very Poor",    "Serious health effects."),
    ("#7f1d1d", "401–500","Severe",       "Emergency conditions."),
]

def render_header():
    st.markdown("""
    <div class="hero">
        <div class="hero-pill">🌿 AI-Powered &nbsp;·&nbsp; India NAAQS</div>
        <h1>Air Quality <span>Predictor</span></h1>
        <p>Enter pollutant concentrations to get an instant AQI prediction with personalised
        health guidance — powered by a Random Forest model trained on India's city-day dataset.</p>
    </div>
    """, unsafe_allow_html=True)


def render_gauge(aqi_value, color):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=aqi_value,
        number={
            "font": {"size": 36, "color": "#ffffff", "family": "Plus Jakarta Sans"},
        },
        gauge={
            "axis": {
                "range": [0, 500],
                "tickwidth": 1,
                "tickcolor": "rgba(255,255,255,0.2)",
                "tickfont": {"color": "rgba(255,255,255,0.4)", "size": 9},
                "nticks": 6,
            },
            "bar": {"color": color, "thickness": 0.22},
            "bgcolor": "rgba(0,0,0,0)",
            "borderwidth": 0,
            "steps": [
                {"range": [0,   50],  "color": "rgba(22,163,74,0.20)"},
                {"range": [50,  100], "color": "rgba(132,204,22,0.20)"},
                {"range": [100, 200], "color": "rgba(245,158,11,0.20)"},
                {"range": [200, 300], "color": "rgba(239,68,68,0.20)"},
                {"range": [300, 400], "color": "rgba(168,85,247,0.20)"},
                {"range": [400, 500], "color": "rgba(127,29,29,0.20)"},
            ],
            "threshold": {
                "line": {"color": color, "width": 3},
                "thickness": 0.75,
                "value": aqi_value,
            },
        },
    ))
    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font={"family": "Plus Jakarta Sans"},
        margin={"t": 16, "b": 0, "l": 24, "r": 24},
        height=170,
    )
    # ✅ Fix 3 — use_container_width deprecated; use use_column_width instead
    st.plotly_chart(fig, config={"displayModeBar": False})


def render_result(aqi_value, category, desc, color, emoji):
    st.markdown(f"""
    <div class="result-card" style="background:rgba(15,23,42,0.92);border-top:3px solid {color};">
        <div class="result-top">
            <div class="result-left">
                <div class="result-dot" style="background:{color};box-shadow:0 0 12px {color}88;"></div>
                <div>
                    <div class="result-cat" style="color:{color}">{category}</div>
                    <div class="result-label">Air Quality Index</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_gauge(aqi_value, color)

    st.markdown(f"""
    <div class="result-lower" style="background:rgba(15,23,42,0.92);border:1px solid rgba(255,255,255,0.08);border-top:none;border-radius:0 0 22px 22px;padding:4px 30px 26px;margin-top:-8px;">
        <div class="result-num" style="color:#ffffff;text-align:center;margin-bottom:14px;">{aqi_value:.1f}</div>
        <div class="aqi-scale">
            <span>0</span><span>100</span><span>200</span><span>300</span><span>400</span><span>500</span>
        </div>
        <div class="result-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)


def render_aqi_scale_card():
    rows = "".join(f"""
    <div class="scale-row">
        <div class="scale-dot" style="background:{c};box-shadow:0 0 6px {c}88;"></div>
        <div class="scale-range">{r}</div>
        <div class="scale-name" style="color:{c}">{name}</div>
        <div class="scale-desc">{d}</div>
    </div>""" for c, r, name, d in AQI_SCALE)
    st.markdown(f"""
    <div class="scale-card">
        <div class="scale-header">📊 &nbsp;AQI Scale Reference</div>
        {rows}
    </div>
    """, unsafe_allow_html=True)


def render_tips(tips, color):
    rows = "".join(f"""
    <div class="tip-row" style="border-left-color:{color};">
        <span class="tip-icon">{icon}</span>
        <div>
            <div class="tip-title">{title}</div>
            <div class="tip-body">{body}</div>
        </div>
    </div>""" for icon, title, body in tips)
    st.markdown(f"""
    <div class="tips-card" style="border-top:3px solid {color};">
        <div class="tips-header">💡 &nbsp;Health Recommendations</div>
        {rows}
    </div>
    """, unsafe_allow_html=True)


def render_placeholder():
    render_aqi_scale_card()
    st.markdown("""
    <div class="placeholder">
        <div class="ph-icon">🌍</div>
        <div class="ph-title">Ready to Analyse</div>
        <p class="ph-text">Fill in the pollutant values on the left and click
        <strong style="color:#63b3ed">Predict AQI</strong> to see your results here.</p>
    </div>
    """, unsafe_allow_html=True)


def render_stats():
    st.markdown("""
    <div class="stats-row">
        <div class="stat-card">
            <div class="stat-icon">🤖</div>
            <div class="stat-title">Random Forest Model</div>
            <div class="stat-text">Trained on Kaggle's India city-day dataset with cross-validation.</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">📊</div>
            <div class="stat-title">12 Pollutant Inputs</div>
            <div class="stat-text">PM2.5, PM10, NO, NO₂, NOx, NH₃, CO, SO₂, O₃, Benzene, Toluene, Xylene.</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">🏥</div>
            <div class="stat-title">Health Guidance</div>
            <div class="stat-text">Personalised tips across 6 AQI categories — Good to Severe.</div>
        </div>
        <div class="stat-card">
            <div class="stat-icon">⚡</div>
            <div class="stat-title">Instant Prediction</div>
            <div class="stat-text">Results in milliseconds with no delays or external API calls.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer">
        <p>Built with <strong>Streamlit</strong> &nbsp;·&nbsp; Model trained on
        <strong>Kaggle City Day Dataset</strong> &nbsp;·&nbsp; India NAAQS Standards</p>
        <p>For informational purposes only. Always consult official monitoring stations for critical decisions.</p>
    </div>
    """, unsafe_allow_html=True)