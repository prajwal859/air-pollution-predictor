# 🌍 Air Pollution (PM2.5) Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pm25-forecast.streamlit.app)

A machine learning web app that predicts **PM2.5 concentration** based on weather conditions and time features. Trained on the Beijing PM2.5 dataset, the app uses a linear regression model to provide real-time predictions.

![App Screenshot](screenshot.png)

## 🚀 Live Demo

Check out the live app: [pm25-forecast.streamlit.app](https://pm25-forecast.streamlit.app)

## 📊 Features

- Predict PM2.5 using:
  - Temperature, Pressure, Dew Point, Wind Speed
  - Snow and Rain indicators
  - Time of day, Month, Season
  - Previous pollution levels (1h and 24h lags)
  - Wind direction (NE, NW, SE, calm)
- Clean, user-friendly interface built with Streamlit
- Instant predictions with air quality category (Good, Moderate, etc.)

## 🛠️ Technologies Used

- **Python** (pandas, numpy, scikit-learn, joblib)
- **Machine Learning**: Linear Regression (best performer), Random Forest, XGBoost
- **Web Framework**: Streamlit
- **Deployment**: Streamlit Community Cloud

## 📁 Dataset

The model was trained on the [Beijing PM2.5 Data Set](https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data) from the UCI Machine Learning Repository. It contains hourly PM2.5 readings along with meteorological data from 2010 to 2014.

## ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/prajwal859/air-pollution-predictor.git
   cd air-pollution-predictor