import pandas as pd

# URLs for COVID-19 time series data from Johns Hopkins University
data_urls = {
    "confirmed": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
    "deaths": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
    "recovered": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
}

def load_covid_data(data_type="confirmed"):
    """
    Load COVID-19 time series data for confirmed cases, deaths, or recoveries.
    
    Parameters:
        data_type (str): One of "confirmed", "deaths", or "recovered".
    
    Returns:
        pd.DataFrame: Processed DataFrame with dates as index and countries as columns.
    """
    if data_type not in data_urls:
        raise ValueError("Invalid data type. Choose from: 'confirmed', 'deaths', 'recovered'")
    
    df = pd.read_csv(data_urls[data_type])
    df = df.drop(columns=['Province/State', 'Lat', 'Long'])
    df = df.groupby('Country/Region').sum()
    df = df.transpose()
    df.index = pd.to_datetime(df.index, format='%m/%d/%y')
    return df

if __name__ == "__main__":
    df_confirmed = load_covid_data("confirmed")
    print(df_confirmed.head())
