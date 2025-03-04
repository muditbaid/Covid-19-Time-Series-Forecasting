import matplotlib.pyplot as plt

def plot_time_series(df, countries):
    """
    Plot time series data for selected countries.
    
    Parameters:
        df (pd.DataFrame): COVID-19 data with dates as index and countries as columns.
        countries (list): List of countries to visualize.
    """
    plt.figure(figsize=(10, 6))
    for country in countries:
        plt.plot(df.index, df[country], label=country)
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.title('COVID-19 Confirmed Cases Over Time')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from data_loader import load_covid_data
    df = load_covid_data("confirmed")
    plot_time_series(df, ['US', 'India', 'Brazil'])
