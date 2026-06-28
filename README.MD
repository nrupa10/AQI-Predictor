# 🌍 Air Quality Prediction System

A professional, production-ready Streamlit web application for predicting Air Quality Index (AQI) using Machine Learning.

---

## 🎯 Overview

This project demonstrates the application of Machine Learning to predict air quality levels based on pollutant measurements. It features a modern dashboard with interactive visualizations, real-time predictions, and health recommendations.

---

## ✨ Features

- **Modern Dashboard** — Glassmorphism UI with full-screen Earth background
- **Real-time Predictions** — Predict AQI from 12 pollutant parameters
- **Interactive Gauge** — Semicircular speedometer showing AQI levels with color coding
- **Health Recommendations** — Contextual health advice based on predicted AQI
- **AQI Scale Reference** — Built-in reference card for all 6 AQI categories
- **Input Validation** — Prevents prediction on empty/zero inputs
- **Responsive Design** — Works seamlessly on desktop and mobile devices

---

## 🛠️ Technology Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Streamlit | Web application framework |
| Scikit-Learn | Machine learning (Random Forest Regressor) |
| Plotly | Interactive speedometer gauge |
| Pandas | Data processing and feature engineering |

---

## 📁 Project Structure

```
AQI-Predictor/
├── app.py              # Main Streamlit application
├── components.py       # UI components (gauge, cards, tips)
├── styles.py           # CSS styling and theming
├── config.py           # App configuration and AQI categories
├── utils.py            # Helper functions (colors, categories)
├── data_loader.py      # Dataset loading and preprocessing
├── data/
│   └── city_day.csv    # India city-day AQI dataset (Kaggle)
├── models/
│   └── aqi_model.pkl   # Trained Random Forest model
├── earth_image.jpg     # Background image
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/AQI-Predictor.git
cd AQI-Predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## 📊 Model Details

- **Algorithm** — Random Forest Regressor
- **Training Data** — Kaggle India City Day AQI Dataset
- **Features** — PM2.5, PM10, NO, NO₂, NOx, NH₃, CO, SO₂, O₃, Benzene, Toluene, Xylene
- **Target** — AQI (Air Quality Index)
- **Split** — 80% train / 20% test, random_state=42

---

## 🏥 AQI Categories

| Range | Category | Health Impact |
|-------|----------|--------------|
| 0–50 | 🟢 Good | Minimal impact |
| 51–100 | 🟡 Satisfactory | Minor breathing discomfort |
| 101–200 | 🟠 Moderate | Breathing discomfort for sensitive people |
| 201–300 | 🔴 Poor | Breathing discomfort for most |
| 301–400 | 🟣 Very Poor | Respiratory illness on prolonged exposure |
| 401–500 | 🟤 Severe | Serious health effects for everyone |

---

## 📌 Notes

- Dataset sourced from [Kaggle — Air Quality Data in India](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)
- For informational purposes only — always consult official monitoring stations for critical decisions
- India NAAQS standards followed for AQI categorisation

---

*Built as part of a college ML project.*