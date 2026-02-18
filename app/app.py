import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Page config
st.set_page_config(page_title="PM2.5 Predictor", layout="centered")
st.title("🌍 Air Pollution (PM2.5) Predictor")
st.markdown("Enter weather conditions and time features to predict PM2.5 concentration.")

# Load model and scaler
@st.cache_resource
def load_model():
    model = joblib.load('models/linear_regression.pkl')
    scaler = joblib.load('models/scaler.pkl')
    return model, scaler

model, scaler = load_model()

# Define feature columns in the exact order used during training
feature_cols = ['TEMP', 'PRES', 'DEWP', 'Iws', 'Is', 'Ir', 
                'hour', 'month', 'season', 'lag_1h', 'lag_24h', 
                'wind_NE', 'wind_NW', 'wind_SE', 'wind_cv']

# Create input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        temp = st.number_input("Temperature (°C)", value=12.0)
        pres = st.number_input("Pressure (hPa)", value=1016.0)
        dewp = st.number_input("Dew Point (°C)", value=2.0)
        iws = st.number_input("Wind Speed (m/s)", value=5.0)
        is_ = st.number_input("Snow (hours)", value=0, step=1)
        ir = st.number_input("Rain (hours)", value=0, step=1)
    
    with col2:
        hour = st.slider("Hour of day", 0, 23, 12)
        month = st.slider("Month", 1, 12, 6)
        season = st.selectbox("Season", [1, 2, 3, 4], format_func=lambda x: ['Winter','Spring','Summer','Fall'][x-1])
        lag_1h = st.number_input("PM2.5 1 hour ago", value=80.0)
        lag_24h = st.number_input("PM2.5 24 hours ago", value=75.0)
    
    st.subheader("Wind Direction")
    wind_dir = st.radio("Choose one:", ["NE", "NW", "SE", "cv"], horizontal=True)
    
    submitted = st.form_submit_button("Predict PM2.5")

if submitted:
    # Create one-hot encoding for wind direction
    wind_ne = 1 if wind_dir == "NE" else 0
    wind_nw = 1 if wind_dir == "NW" else 0
    wind_se = 1 if wind_dir == "SE" else 0
    wind_cv = 1 if wind_dir == "cv" else 0
    
    # Build input array
    input_data = [[temp, pres, dewp, iws, is_, ir, hour, month, season,
                   lag_1h, lag_24h, wind_ne, wind_nw, wind_se, wind_cv]]
    input_df = pd.DataFrame(input_data, columns=feature_cols)
    
    # Scale and predict
    scaled = scaler.transform(input_df)
    prediction = model.predict(scaled)[0]
    
    st.success(f"### Predicted PM2.5: **{prediction:.1f} µg/m³**")
    
    # Optional: Add a gauge or color coding
    if prediction < 50:
        st.info("🟢 Good air quality")
    elif prediction < 100:
        st.warning("🟡 Moderate")
    elif prediction < 150:
        st.warning("🟠 Unhealthy for sensitive groups")
    else:
        st.error("🔴 Unhealthy")