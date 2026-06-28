# 🌍 Air Quality Prediction System

A Machine Learning powered web application that predicts the **Air Quality Index (AQI)** using pollutant concentration data. Built with **Python**, **Streamlit**, **Scikit-learn**, and **Plotly**, the application provides real-time AQI predictions, interactive visualizations, and health recommendations.

---

Features

* Predict AQI using **12 air pollutant parameters**
* Interactive AQI speedometer gauge
* Health recommendations based on predicted AQI
* Modern Glassmorphism user interface
* AQI category reference with color coding
* Input validation to prevent invalid predictions
* Responsive design for desktop and mobile devices

---

Technical Implementation

* Machine Learning model trained using **Random Forest Regressor**
* Built with **Python** and **Streamlit**
* Interactive visualizations using **Plotly**
* Data preprocessing using **Pandas**
* Model serialization using **Pickle (.pkl)**

---

Project Structure

```
AQI-Predictor/
│
├── app.py                    # Main Streamlit application
├── components.py             # UI components
├── styles.py                 # CSS styling
├── config.py                 # AQI categories & configuration
├── utils.py                  # Helper functions
├── data_loader.py            # Dataset preprocessing
│
├── models/
│   └── aqi_model.pkl         # Trained ML model
│
├── data/
│   └── city_day.csv          # AQI dataset
│
├── earth_image.jpg           # Background image
├── requirements.txt
└── README.md
```

---

Getting Started

1. Clone the Repository

```bash
git clone https://github.com/your-username/AQI-Predictor.git
```

2. Navigate to the Project

```bash
cd AQI-Predictor
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

 Machine Learning Model

The prediction model is trained using the **Random Forest Regressor** algorithm on the **India Air Quality Dataset (2015–2020)**.

### Input Features

* PM2.5
* PM10
* NO
* NO₂
* NOx
* NH₃
* CO
* SO₂
* O₃
* Benzene
* Toluene
* Xylene

### Target

* Air Quality Index (AQI)

### Dataset

* India Air Quality Dataset (2015–2020)
* Missing values handled during preprocessing
* 80% Training
* 20% Testing

---

AQI Categories

| AQI     | Category        |
| ------- | --------------- |
| 0–50    | 🟢 Good         |
| 51–100  | 🟡 Satisfactory |
| 101–200 | 🟠 Moderate     |
| 201–300 | 🔴 Poor         |
| 301–400 | 🟣 Very Poor    |
| 401–500 | 🟤 Severe       |

---

 Application Workflow

1. User enters pollutant concentration values.
2. Input data is validated.
3. The trained Random Forest model predicts AQI.
4. AQI category is determined.
5. Interactive gauge displays the AQI.
6. Health recommendations are shown based on the prediction.

---
Dependencies

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Plotly
* Joblib / Pickle

Install using:

```bash
pip install -r requirements.txt
```

---

Notes

* Dataset sourced from the **India Air Quality Dataset (2015–2020)**.
* This project is intended for educational and demonstration purposes.
* Actual AQI values should always be verified using official environmental monitoring agencies.

---
Machine Learning | Python | Data Science
