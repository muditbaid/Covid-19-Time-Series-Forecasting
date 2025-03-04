from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def arima_forecast(df, country, order=(5,1,0), steps=30):
    """
    Fit an ARIMA model and forecast COVID-19 cases.
    
    Parameters:
        df (pd.DataFrame): Time series data.
        country (str): Country for forecasting.
        order (tuple): ARIMA order (p, d, q).
        steps (int): Number of days to forecast.
    """
    series = df[country]
    model = ARIMA(series, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    
    plt.figure(figsize=(10, 6))
    plt.plot(series, label='Actual')
    plt.plot(forecast, label='Forecast', color='red')
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.title(f'COVID-19 Forecast for {country}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from data_loader import load_covid_data
    df = load_covid_data("confirmed")
    arima_forecast(df, 'US')
