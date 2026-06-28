import pandas as pd
import os

def load_data():
    """Load and preprocess the air quality data"""
    try:
        data_path = os.path.join("data", "city_day.csv")
        
        if not os.path.exists(data_path):
            # Create sample data if file doesn't exist
            create_sample_data()
        
        df = pd.read_csv(data_path)
        
        # Basic preprocessing
        # Convert date column if exists
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
        
        # Handle missing values
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        
        return df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def create_sample_data():
    """Create sample air quality data for testing"""
    import numpy as np
    from datetime import datetime, timedelta
    
    # Generate dates
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    
    # Generate sample data
    np.random.seed(42)
    n_samples = len(dates)
    
    data = {
        'Date': dates,
        'City': np.random.choice(['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata'], n_samples),
        'PM2.5': np.random.uniform(10, 300, n_samples),
        'PM10': np.random.uniform(20, 400, n_samples),
        'NO2': np.random.uniform(5, 200, n_samples),
        'SO2': np.random.uniform(2, 150, n_samples),
        'CO': np.random.uniform(0.1, 20, n_samples),
        'O3': np.random.uniform(5, 200, n_samples),
        'AQI': np.random.uniform(20, 400, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Save to CSV
    os.makedirs('data', exist_ok=True)
    df.to_csv(os.path.join('data', 'city_day.csv'), index=False)
    
    return df