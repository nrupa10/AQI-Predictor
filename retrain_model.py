import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("data/city_day.csv")

features = [
    "PM2.5", "PM10", "NO", "NO2", "NOx",
    "NH3", "CO", "SO2", "O3",
    "Benzene", "Toluene", "Xylene"
]

df_clean = df.dropna(subset=["AQI"])
df_clean = df_clean.dropna(subset=features)

X = df_clean[features]
y = df_clean["AQI"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

predictions = rf_model.predict(X_test)
print(f"R²  : {r2_score(y_test, predictions):.4f}")
print(f"MAE : {mean_absolute_error(y_test, predictions):.4f}")

with open("models/aqi_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)

print("\nModel saved successfully!")