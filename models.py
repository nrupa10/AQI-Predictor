import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import os
import streamlit as st

# Define all 12 features that the model expects
MODEL_FEATURES = [
    'PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3',
    'Benzene', 'Toluene', 'Xylene', 'AQI_Bucket',
    'City_encoded', 'Month'
]

def load_model():
    """Load the trained AQI model"""
    try:
        model_path = os.path.join("models", "aqi_model.pkl")
        with open(model_path, "rb") as file:
            model_data = pickle.load(file)
        return model_data
    except FileNotFoundError:
        st.warning("⚠️ Model file not found. Training new model...")
        return train_model()
    except Exception as e:
        st.error(f"⚠️ Error loading model: {str(e)}")
        return None

def train_model():
    """Train the AQI prediction model with 12 features"""
    try:
        # Load data
        data_path = os.path.join("data", "city_day.csv")
        
        if not os.path.exists(data_path):
            create_sample_data()
            
        df = pd.read_csv(data_path)
        
        # Create all 12 features
        features_df = pd.DataFrame()
        
        # Pollutant features (6)
        pollutant_cols = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
        for col in pollutant_cols:
            if col in df.columns:
                features_df[col] = df[col].fillna(df[col].mean())
            else:
                features_df[col] = np.random.uniform(10, 100, len(df))
        
        # Additional chemical features (3)
        chemical_cols = ['Benzene', 'Toluene', 'Xylene']
        for col in chemical_cols:
            if col in df.columns:
                features_df[col] = df[col].fillna(df[col].mean())
            else:
                features_df[col] = np.random.uniform(0, 10, len(df))
        
        # AQI Bucket (categorical - encode)
        if 'AQI_Bucket' in df.columns:
            bucket_map = {'Good': 0, 'Satisfactory': 1, 'Moderate': 2, 
                         'Poor': 3, 'Very Poor': 4, 'Severe': 5}
            features_df['AQI_Bucket'] = df['AQI_Bucket'].map(bucket_map).fillna(2)
        else:
            features_df['AQI_Bucket'] = np.random.randint(0, 6, len(df))
        
        # City encoded (using City column if exists)
        if 'City' in df.columns:
            city_map = {city: i for i, city in enumerate(df['City'].unique())}
            features_df['City_encoded'] = df['City'].map(city_map).fillna(0)
        else:
            features_df['City_encoded'] = np.random.randint(0, 10, len(df))
        
        # Month (from Date column if exists)
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            features_df['Month'] = df['Date'].dt.month
        else:
            features_df['Month'] = np.random.randint(1, 13, len(df))
        
        # Target variable (AQI)
        if 'AQI' in df.columns:
            y = df['AQI'].fillna(df['AQI'].mean())
        else:
            y = np.random.uniform(20, 400, len(df))
        
        # Scale features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(features_df)
        
        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_scaled, y)
        
        # Save model with all metadata
        model_data = {
            'model': model,
            'feature_names': list(features_df.columns),
            'scaler': scaler,
            'feature_columns': list(features_df.columns)
        }
        
        os.makedirs('models', exist_ok=True)
        model_path = os.path.join("models", "aqi_model.pkl")
        with open(model_path, "wb") as file:
            pickle.dump(model_data, file)
        
        st.success("✅ Model trained successfully!")
        return model_data
    except Exception as e:
        st.error(f"❌ Error training model: {str(e)}")
        return None

def prepare_features(user_inputs):
    """
    Prepare all 12 features from user inputs
    user_inputs: dict with keys 'pm25', 'pm10', 'no2', 'so2', 'co', 'o3'
    """
    # Create dataframe with all 12 features
    features_df = pd.DataFrame(columns=MODEL_FEATURES)
    features_df.loc[0] = 0  # Initialize with zeros
    
    # 1. Pollutant features (from user input)
    features_df['PM2.5'] = user_inputs.get('pm25', 50)
    features_df['PM10'] = user_inputs.get('pm10', 80)
    features_df['NO2'] = user_inputs.get('no2', 30)
    features_df['SO2'] = user_inputs.get('so2', 20)
    features_df['CO'] = user_inputs.get('co', 2)
    features_df['O3'] = user_inputs.get('o3', 40)
    
    # 2. Chemical features (using default values or estimating from pollutants)
    # These can be estimated from PM values or use defaults
    features_df['Benzene'] = 0.5 + (features_df['PM2.5'] * 0.02)  # Rough estimate
    features_df['Toluene'] = 0.7 + (features_df['PM10'] * 0.015)  # Rough estimate
    features_df['Xylene'] = 0.3 + (features_df['PM2.5'] * 0.01)   # Rough estimate
    
    # 3. Categorical features
    # AQI_Bucket - estimate from PM values
    avg_pm = (features_df['PM2.5'] + features_df['PM10']) / 2
    if avg_pm < 30:
        features_df['AQI_Bucket'] = 0  # Good
    elif avg_pm < 60:
        features_df['AQI_Bucket'] = 1  # Satisfactory
    elif avg_pm < 90:
        features_df['AQI_Bucket'] = 2  # Moderate
    elif avg_pm < 120:
        features_df['AQI_Bucket'] = 3  # Poor
    elif avg_pm < 250:
        features_df['AQI_Bucket'] = 4  # Very Poor
    else:
        features_df['AQI_Bucket'] = 5  # Severe
    
    # City_encoded (default to 0 - Delhi)
    features_df['City_encoded'] = 0
    
    # Month (current month)
    from datetime import datetime
    features_df['Month'] = datetime.now().month
    
    return features_df

def predict_aqi(model_data, user_inputs):
    """Predict AQI using the trained model with 12 features"""
    if model_data is None:
        # Fallback to simple calculation
        return calculate_aqi_from_pollutants(user_inputs)
    
    try:
        # Prepare all 12 features
        features_df = prepare_features(user_inputs)
        
        # Check if model_data has feature names
        if isinstance(model_data, dict):
            model = model_data['model']
            scaler = model_data.get('scaler', None)
            feature_names = model_data.get('feature_names', MODEL_FEATURES)
            
            # Ensure features are in the right order
            if scaler is not None:
                X_scaled = scaler.transform(features_df)
                prediction = model.predict(X_scaled)
            else:
                prediction = model.predict(features_df)
            
            return max(0, prediction[0])  # Ensure non-negative AQI
        else:
            # Old format - try to predict with just the model
            prediction = model_data.predict(features_df)
            return max(0, prediction[0])
            
    except Exception as e:
        st.warning(f"⚠️ Prediction error: {str(e)}. Using simplified calculation.")
        return calculate_aqi_from_pollutants(user_inputs)

def calculate_aqi_from_pollutants(user_inputs):
    """
    Calculate AQI from individual pollutant concentrations (simplified)
    """
    pm25 = user_inputs.get('pm25', 50)
    pm10 = user_inputs.get('pm10', 80)
    no2 = user_inputs.get('no2', 30)
    so2 = user_inputs.get('so2', 20)
    co = user_inputs.get('co', 2)
    o3 = user_inputs.get('o3', 40)
    
    # Calculate individual AQI values (simplified)
    def calc_pm25_aqi(value):
        if value <= 30: return value * 1.67
        elif value <= 60: return 50 + (value - 30) * 1.67
        elif value <= 90: return 100 + (value - 60) * 1.67
        elif value <= 120: return 150 + (value - 90) * 1.67
        elif value <= 250: return 200 + (value - 120) * 0.77
        else: return 300 + (value - 250) * 0.8
    
    def calc_pm10_aqi(value):
        if value <= 50: return value * 1
        elif value <= 100: return 50 + (value - 50)
        elif value <= 250: return 100 + (value - 100) * 0.33
        elif value <= 350: return 150 + (value - 250) * 0.5
        else: return 200 + (value - 350) * 0.67
    
    # Calculate AQI (take the max of individual AQIs)
    aqi_values = [
        calc_pm25_aqi(pm25),
        calc_pm10_aqi(pm10),
        no2 * 0.5,
        so2 * 0.3,
        co * 10,
        o3 * 0.4
    ]
    
    # Weighted average
    weights = [0.3, 0.25, 0.15, 0.1, 0.1, 0.1]
    aqi = sum(aqi_values[i] * weights[i] for i in range(len(aqi_values)))
    
    # Cap at 500
    return min(max(aqi, 0), 500)

def create_sample_data():
    """Create sample air quality data with 12 features"""
    np.random.seed(42)
    n_samples = 1000
    
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')[:n_samples]
    
    data = {
        'Date': dates,
        'City': np.random.choice(['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata'], n_samples),
        'PM2.5': np.random.uniform(10, 300, n_samples),
        'PM10': np.random.uniform(20, 400, n_samples),
        'NO2': np.random.uniform(5, 200, n_samples),
        'SO2': np.random.uniform(2, 150, n_samples),
        'CO': np.random.uniform(0.1, 20, n_samples),
        'O3': np.random.uniform(5, 200, n_samples),
        'Benzene': np.random.uniform(0, 10, n_samples),
        'Toluene': np.random.uniform(0, 15, n_samples),
        'Xylene': np.random.uniform(0, 8, n_samples),
        'AQI': np.random.uniform(20, 400, n_samples),
        'AQI_Bucket': np.random.choice(['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe'], n_samples)
    }
    
    df = pd.DataFrame(data)
    
    os.makedirs('data', exist_ok=True)
    df.to_csv(os.path.join('data', 'city_day.csv'), index=False)
    
    return df

# Initialize model on import
model_data = None
try:
    if os.path.exists(os.path.join("models", "aqi_model.pkl")):
        with open(os.path.join("models", "aqi_model.pkl"), "rb") as file:
            model_data = pickle.load(file)
    else:
        print("Training model with 12 features...")
        model_data = train_model()
except Exception as e:
    print(f"Error initializing model: {str(e)}")