import base64, os

def _b64(path):
    if os.path.exists(path):
        with open(path,"rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

def get_css():
    b64 = _b64("earth_image.jpg")
    if b64:
        bg = f"background-image:url('data:image/jpeg;base64,{b64}');background-size:cover;background-position:center;background-attachment:fixed;"
    else:
        bg = "background:#060c1c;"

    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}

/* ── Background ── */
.stApp{{{bg}min-height:100vh;font-family:'Plus Jakarta Sans',sans-serif;}}
.stApp::before{{content:'';position:fixed;inset:0;background:rgba(4,8,20,0.58);z-index:0;pointer-events:none;}}
.stApp>*{{position:relative;z-index:1;}}

/* ── Hide chrome ── */
#MainMenu,footer,header,.stDeployButton{{visibility:hidden!important;}}
.block-container{{padding:0!important;max-width:100%!important;}}
section[data-testid="stSidebar"]{{display:none;}}

/* ── NUMBER INPUT ── */
div[data-testid="stNumberInput"],
div[data-testid="stNumberInput"] > div,
div[data-testid="stNumberInput"] > div > div,
div[data-testid="stNumberInput"] > div > div > div {{
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}}
div[data-testid="stNumberInput"] input {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    color: #e2e8f0 !important;
    background: rgba(255,255,255,0.0) !important;
    background-color: transparent !important;
    border: none !important;
    border-bottom: 2px solid rgba(255,255,255,0.12) !important;
    border-radius: 0 !important;
    padding: 8px 4px 8px 0 !important;
    box-shadow: none !important;
    outline: none !important;
    caret-color: #63b3ed !important;
    transition: border-color .2s !important;
    width: 100% !important;
    -webkit-text-fill-color: #e2e8f0 !important;
}}
div[data-testid="stNumberInput"] input:focus {{
    border-bottom-color: #63b3ed !important;
    background: transparent !important;
    background-color: transparent !important;
    box-shadow: none !important;
    outline: none !important;
    -webkit-text-fill-color: #e2e8f0 !important;
    color: #e2e8f0 !important;
}}
div[data-testid="stNumberInput"] input:-webkit-autofill,
div[data-testid="stNumberInput"] input:-webkit-autofill:hover,
div[data-testid="stNumberInput"] input:-webkit-autofill:focus {{
    -webkit-text-fill-color: #e2e8f0 !important;
    -webkit-box-shadow: 0 0 0px 1000px transparent inset !important;
    transition: background-color 5000s ease-in-out 0s;
    background: transparent !important;
}}
div[data-testid="stNumberInput"] button {{
    background: transparent !important;
    border: none !important;
    border-bottom: 2px solid rgba(255,255,255,0.12) !important;
    border-radius: 0 !important;
    color: #4a5568 !important;
    box-shadow: none !important;
    transition: color .15s !important;
    padding: 8px 6px !important;
}}
div[data-testid="stNumberInput"] button:hover {{
    color: #63b3ed !important;
    background: transparent !important;
    border-bottom-color: #63b3ed !important;
}}
div[data-testid="stNumberInput"] button svg {{
    fill: currentColor !important;
    stroke: currentColor !important;
}}
/* ★ Suggestion 4 — clean labels, no emoji clutter ★ */
div[data-testid="stNumberInput"] label p {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: .68rem !important;
    font-weight: 700 !important;
    color: #718096 !important;
    letter-spacing: .1em !important;
    text-transform: uppercase !important;
    margin-bottom: 2px !important;
}}

/* ── FORM container ── */
div[data-testid="stForm"],
div[data-testid="stForm"] > div {{
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}}

/* ── SUBMIT BUTTON — ★ Suggestion 8: float shadow + hover lift ★ ── */
.stFormSubmitButton > button,
div[data-testid="stForm"] .stFormSubmitButton button {{
    width:100%!important;
    font-family:'Plus Jakarta Sans',sans-serif!important;
    font-size:.95rem!important;
    font-weight:700!important;
    letter-spacing:.06em!important;
    color:#fff!important;
    background:linear-gradient(135deg,#2E8BFF,#1a6fd8)!important;
    border:none!important;
    border-radius:14px!important;
    padding:15px 20px!important;
    cursor:pointer!important;
    transition:all .25s ease!important;
    margin-top:24px!important;
    /* floating shadow */
    box-shadow:0 6px 28px rgba(46,139,255,.45), 0 2px 8px rgba(0,0,0,.3)!important;
}}
.stFormSubmitButton > button:hover {{
    background:linear-gradient(135deg,#52A7FF,#2E8BFF)!important;
    transform:translateY(-3px)!important;
    box-shadow:0 12px 40px rgba(46,139,255,.60), 0 4px 12px rgba(0,0,0,.3)!important;
}}

/* ── HERO ── */
.hero{{padding:60px 6vw 44px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.06);}}
.hero-pill{{display:inline-flex;align-items:center;gap:6px;background:rgba(99,179,237,0.12);border:1px solid rgba(99,179,237,0.28);color:#63b3ed;padding:5px 16px;border-radius:999px;font-size:11px;font-weight:700;letter-spacing:.13em;text-transform:uppercase;margin-bottom:22px;}}
.hero h1{{font-size:clamp(2.4rem,5vw,4rem);font-weight:800;color:#fff;letter-spacing:-.03em;line-height:1.08;margin-bottom:16px;}}
.hero h1 span{{background:linear-gradient(135deg,#63b3ed,#90cdf4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.hero p{{color:rgba(255,255,255,0.85);font-size:.97rem;max-width:540px;margin:0 auto;line-height:1.75;}}

/* ── PAGE WRAP ── */
.page-wrap{{max-width:1300px;margin:0 auto;padding:40px 6vw 28px;}}

/* ── SECTION PANEL — ★ Suggestion 5: higher opacity ★ ── */
.panel{{background:rgba(15,23,42,0.88);border:1px solid rgba(255,255,255,0.08);border-radius:22px;padding:30px 30px 22px;backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);margin-bottom:6px;}}
.panel-eyebrow{{font-size:.62rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#718096;margin-bottom:6px;}}
.panel-heading{{font-size:1.3rem;font-weight:700;color:#f0f4f8;margin-bottom:5px;letter-spacing:-.01em;}}
.panel-sub{{font-size:.80rem;color:rgba(255,255,255,0.65);line-height:1.55;}}

/* ── GROUP LABELS ── */
.group-label{{font-size:.62rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#718096;padding:22px 0 12px;border-top:1px solid rgba(255,255,255,0.05);margin-top:8px;}}
.group-label:first-child{{border-top:none;padding-top:6px;}}

/* ── RESULT CARD — ★ Suggestion 5: higher opacity ★ ── */
.result-card{{border-radius:22px 22px 0 0;padding:28px 30px 16px;backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,0.08);border-bottom:none;margin-bottom:0;}}
.result-lower{{backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);}}
.result-top{{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:4px;}}
.result-left{{display:flex;align-items:center;gap:16px;}}
.result-dot{{width:44px;height:44px;border-radius:50%;flex-shrink:0;}}
.result-cat{{font-size:1.7rem;font-weight:800;line-height:1.1;letter-spacing:-.02em;}}
.result-label{{font-size:.65rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#718096;margin-top:5px;}}
/* ★ Suggestion 6 — AQI number in white ★ */
.result-num{{font-size:3.2rem;font-weight:800;letter-spacing:-.04em;line-height:1;color:#ffffff!important;}}
.aqi-scale{{display:flex;justify-content:space-between;font-size:.6rem;color:#718096;font-weight:600;margin-bottom:16px;}}
.result-desc{{font-size:.84rem;color:rgba(255,255,255,0.75);line-height:1.65;padding-top:16px;border-top:1px solid rgba(255,255,255,0.05);}}

/* ── AQI SCALE CARD — ★ Suggestion 5: higher opacity ★ ── */
.scale-card{{background:rgba(15,23,42,0.88);border:1px solid rgba(255,255,255,0.08);border-radius:22px;padding:24px 28px;backdrop-filter:blur(18px);margin-bottom:18px;}}
.scale-header{{font-size:.62rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#718096;margin-bottom:16px;}}
.scale-row{{display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid rgba(255,255,255,0.04);}}
.scale-row:last-child{{border-bottom:none;}}
.scale-dot{{width:11px;height:11px;border-radius:50%;flex-shrink:0;}}
.scale-range{{font-size:.72rem;font-weight:700;color:#a0aec0;width:60px;flex-shrink:0;}}
.scale-name{{font-size:.78rem;font-weight:700;flex:1;}}
.scale-desc{{font-size:.68rem;color:rgba(255,255,255,0.55);}}

/* ── TIPS CARD — ★ Suggestion 9: shown before scale ★ — ★ Suggestion 5: higher opacity ★ ── */
.tips-card{{background:rgba(15,23,42,0.88);border:1px solid rgba(255,255,255,0.08);border-radius:22px;padding:26px 30px;backdrop-filter:blur(18px);margin-bottom:18px;}}
.tips-header{{font-size:.62rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#718096;margin-bottom:18px;}}
.tip-row{{display:flex;align-items:flex-start;gap:14px;padding:13px 0 13px 14px;border-bottom:1px solid rgba(255,255,255,0.05);border-left:3px solid transparent;margin-left:-14px;transition:border-color .2s;}}
.tip-row:last-child{{border-bottom:none;}}
.tip-icon{{font-size:1.25rem;flex-shrink:0;margin-top:1px;}}
.tip-title{{font-size:.84rem;font-weight:700;color:rgba(255,255,255,0.9);margin-bottom:3px;}}
.tip-body{{font-size:.76rem;color:rgba(255,255,255,0.60);line-height:1.55;}}

/* ── PLACEHOLDER — ★ Suggestion 5: higher opacity ★ ── */
.placeholder{{background:rgba(15,23,42,0.88);border:1px dashed rgba(255,255,255,0.08);border-radius:22px;padding:70px 32px;text-align:center;backdrop-filter:blur(18px);}}
.ph-icon{{font-size:3rem;margin-bottom:16px;opacity:.35;}}
.ph-title{{font-size:1.05rem;font-weight:700;color:#718096;margin-bottom:10px;}}
.ph-text{{font-size:.82rem;color:rgba(255,255,255,0.45);line-height:1.65;max-width:270px;margin:0 auto;}}

/* ── STATS ROW — ★ Suggestion 5: higher opacity ★ ── */
.stats-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:40px;}}
.stat-card{{background:rgba(15,23,42,0.88);border:1px solid rgba(255,255,255,0.08);border-radius:18px;padding:24px;text-align:center;backdrop-filter:blur(18px);transition:border-color .2s,transform .2s;}}
.stat-card:hover{{border-color:rgba(99,179,237,0.25);transform:translateY(-2px);}}
.stat-icon{{font-size:1.6rem;margin-bottom:10px;}}
.stat-title{{font-size:.80rem;font-weight:700;color:#cbd5e0;margin-bottom:5px;}}
.stat-text{{font-size:.72rem;color:rgba(255,255,255,0.50);line-height:1.55;}}

/* ── FOOTER ── */
.footer{{text-align:center;padding:32px 6vw;border-top:1px solid rgba(255,255,255,0.05);margin-top:10px;}}
.footer p{{font-size:.74rem;color:rgba(255,255,255,0.40);line-height:2.0;}}
.footer strong{{color:rgba(255,255,255,0.60);font-weight:600;}}

/* ── AQI value animation ── */
@keyframes countUp {{
    from {{ opacity:0; transform:translateY(8px); }}
    to   {{ opacity:1; transform:translateY(0); }}
}}
.result-num {{ animation: countUp .5s ease-out both; }}

@media(max-width:768px){{.stats-row{{grid-template-columns:repeat(2,1fr);}}}}
</style>
"""