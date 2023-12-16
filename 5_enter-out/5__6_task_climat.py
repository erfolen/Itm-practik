import pandas as pd
from matplotlib import pyplot as plt


year = 2012
month = 6
url_template = f'https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data'

weather_iuny = pd.read_csv(url_template, index_col='Date/Time (LST)', parse_dates=True)

print(weather_iuny)
print(weather_iuny.columns)
weather_iuny['Temp (°C)'].plot()
plt.show()

weather_iuny.to_csv('weather.csv')
