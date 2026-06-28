PAGE_CONFIG = {
    "page_title": "AQI Predictor",
    "page_icon": "🌿",
    "layout": "wide",
    "initial_sidebar_state": "collapsed",
}
MODEL_PATH = "models/aqi_model.pkl"
FEATURE_COLUMNS = ["PM2.5","PM10","NO","NO2","NOx","NH3","CO","SO2","O3","Benzene","Toluene","Xylene"]
AQI_CATEGORIES = {
    "Good":         {"range":(0,50),    "desc":"Air quality is satisfactory with little or no risk."},
    "Satisfactory": {"range":(51,100),  "desc":"Acceptable quality; minor concern for sensitive groups."},
    "Moderate":     {"range":(101,200), "desc":"Sensitive individuals may experience health effects."},
    "Poor":         {"range":(201,300), "desc":"Everyone may begin to experience adverse health effects."},
    "Very Poor":    {"range":(301,400), "desc":"Health alert — serious effects for the general population."},
    "Severe":       {"range":(401,999), "desc":"Emergency conditions — entire population seriously affected."},
}