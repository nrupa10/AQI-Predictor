from config import AQI_CATEGORIES

COLOR_MAP = {
    "Good":"#16a34a","Satisfactory":"#65a30d","Moderate":"#ca8a04",
    "Poor":"#ea580c","Very Poor":"#dc2626","Severe":"#9333ea",
}
EMOJI_MAP = {
    "Good":"😊","Satisfactory":"🙂","Moderate":"😐",
    "Poor":"😷","Very Poor":"🤢","Severe":"☠️",
}
HEALTH_TIPS = {
    "Good":[
        ("🚴","Great for outdoor exercise","Perfect conditions for running, cycling, or any sport."),
        ("🪟","Open your windows","Let fresh air circulate freely through your home."),
        ("🌿","Add indoor plants","Greenery helps maintain good air quality indoors."),
        ("☀️","No restrictions","Spend as much time outside as you like today."),
    ],
    "Satisfactory":[
        ("💧","Stay hydrated","Water helps your body process minor pollutants."),
        ("🏠","Run air purifiers","HEPA filters keep indoor air clean."),
        ("⏱️","Moderate intense activity","Sensitive individuals should ease up on strenuous exertion."),
        ("🌬️","Ventilate in the morning","Air is typically cleaner in early morning hours."),
    ],
    "Moderate":[
        ("😷","Sensitive groups: be cautious","Children, elderly, and asthma sufferers should limit outdoor time."),
        ("🪟","Close windows at peak hours","Avoid ventilating during heavy traffic periods."),
        ("💊","Keep inhalers handy","Essential for anyone with respiratory conditions."),
        ("🌿","Use N95 mask outside","Wear respiratory protection for extended outdoor stays."),
    ],
    "Poor":[
        ("🚨","Limit outdoor exertion","Everyone should reduce prolonged physical activity outside."),
        ("😷","Wear an N95/N99 mask","Proper protection is essential when outdoors."),
        ("🏠","Stay indoors","Keep windows and doors closed."),
        ("📞","Seek medical advice","Contact a doctor if you experience any breathing difficulty."),
    ],
    "Very Poor":[
        ("🚫","Avoid all outdoor activity","Do not exercise or spend time outside unnecessarily."),
        ("🔒","Seal your home","Close all windows, doors, and ventilation intakes."),
        ("😷","Mandatory N95/N99 mask","Required even for brief outdoor exposure."),
        ("🏥","Consult a doctor","Vulnerable individuals should seek guidance immediately."),
    ],
    "Severe":[
        ("🚨","EMERGENCY — stay indoors","Do not go outside under any circumstances."),
        ("🏥","Seek immediate medical help","Get urgent care for breathing trouble or chest pain."),
        ("😷","Full respiratory protection","Required if outdoor exposure is unavoidable."),
        ("📻","Follow official advisories","Monitor health authority announcements closely."),
    ],
}

def get_aqi_category(aqi):
    for cat, info in AQI_CATEGORIES.items():
        lo, hi = info["range"]
        if lo <= aqi <= hi:
            return cat, info["desc"]
    return "Severe", AQI_CATEGORIES["Severe"]["desc"]

def get_health_tips(cat): return HEALTH_TIPS.get(cat, HEALTH_TIPS["Good"])
def get_aqi_color(cat):   return COLOR_MAP.get(cat, "#16a34a")
def get_aqi_emoji(cat):   return EMOJI_MAP.get(cat, "😊")