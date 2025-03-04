from data_loader import load_covid_data
from visualization import plot_time_series
from forecasting import arima_forecast
from evaluation import evaluate_arima

if __name__ == "__main__":
    # Load confirmed cases data
    df = load_covid_data("confirmed")
    
    # Visualize time series data
    plot_time_series(df, ['US', 'India', 'Brazil'])
    
    # Perform ARIMA forecasting
    arima_forecast(df, 'US')
    
    # Evaluate ARIMA model performance
    evaluate_arima(df, 'US')
