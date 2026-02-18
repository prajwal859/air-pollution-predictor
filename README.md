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

2. **Create and activate a virtual environment**
  ```bash
  python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
  ```bash
  pip install -r requirements.txt

4. **Run the Streamlit app**
  ```bash
  streamlit run app/app.py

## Model Performance
| Model              | MAE   | RMSE  | R²   |
|--------------------|-------|-------|------|
| Linear Regression  | 12.73 | 22.88 | 0.94 |
| Random Forest      | 13.31 | 24.17 | 0.94 |
| XGBoost            | 12.92 | 25.05 | 0.93 |

## 📝 How to Use

1. Adjust the input sliders and number inputs for weather conditions.
2. Select wind direction.
3. Click **Predict PM2.5**.
4. The predicted value and air quality category will appear.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the (https://github.com/prajwal859/air-pollution-predictor/issues).

## 📄 License

This project is MIT licensed.

## 🙏 Acknowledgements

- UCI Machine Learning Repository for the dataset
- Streamlit for the amazing framework