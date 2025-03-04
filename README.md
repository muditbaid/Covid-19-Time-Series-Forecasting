# COVID-19 Time Series Forecasting

This repository provides a **time series analysis and forecasting** pipeline for COVID-19 cases using **ARIMA models**. It fetches real-time data from **Johns Hopkins University**, visualizes trends, and predicts future cases.

## 📌 Project Overview
- **Fetches real-time COVID-19 data** from GitHub.
- **Visualizes** confirmed cases for selected countries.
- **Performs time series decomposition** to analyze trends.
- **Forecasts future cases** using ARIMA models.
- **Evaluates forecast performance** using Mean Squared Error (MSE).

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/muditbaid/Covid-19-Time-Series-Forecasting.git
cd Covid-19-Time-Series-Forecasting
```

### 2️⃣ Install Dependencies
Create a virtual environment and install required libraries:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### 3️⃣ Run the Pipeline
```python
python covid_time_series.py
```

## 📂 Repository Structure
```
.
├── src/                  # Core scripts
│   ├── data_loader.py    # Loads and preprocesses COVID-19 data
│   ├── visualization.py  # Generates time series plots
│   ├── forecasting.py    # ARIMA model training & forecasting
│   ├── evaluation.py     # Model performance evaluation
├── notebooks/            # Jupyter notebooks for analysis
├── results/              # Stores model outputs & forecasts
├── README.md             # Project documentation
├── requirements.txt      # Dependencies
└── covid_time_series.py  # Main Python script
```

## 🛠️ Future Improvements
- Test **LSTM and Prophet models** for better forecasting.
- Automate real-time updates using GitHub Actions.
- Extend analysis to **regional and state-wise** forecasting.

## 📌 References
- [Johns Hopkins COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19)
- [StatsModels ARIMA](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)
- [Matplotlib Visualization](https://matplotlib.org/)

## 📝 License
This project is for research and educational purposes. Free to use with attribution.

---
Feel free to contribute by submitting a pull request! 🚀
