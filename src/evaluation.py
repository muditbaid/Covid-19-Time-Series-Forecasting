from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def evaluate_arima(df, country, order=(5,1,0), train_ratio=0.8):
    """
    Evaluate ARIMA model on COVID-19 time series data.
    
    Parameters:
        df (pd.DataFrame): Time series data.
        country (str): Country for evaluation.
        order (tuple): ARIMA order (p, d, q).
        train_ratio (float): Ratio of data used for training.
    """
    series = df[country]
    train_size = int(len(series) * train_ratio)
    train, test = series[:train_size], series[train_size:]
    
    model = ARIMA(train, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=len(test))
    
    mse = mean_squared_error(test, forecast)
    print(f'Mean Squared Error: {mse}')
    
    plt.figure(figsize=(10, 6))
    plt.plot(train, label='Training Data')
    plt.plot(test, label='Test Data')
    plt.plot(test.index, forecast, label='Forecast', color='red')
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.title(f'COVID-19 Forecast Evaluation for {country}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from data_loader import load_covid_data
    df = load_covid_data("confirmed")
    evaluate_arima(df, 'US')
