import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 10)  # Размер картинок

data_path = Path(Path.cwd(), 'dataset', 'bikes.csv')
#"""encoding='latin1'"""
data = pd.read_csv(data_path, index_col='Date', parse_dates=['Date'], dayfirst=True)

def articl_1():
    print(data[['Berri 1', 'Cute-Sainte-Catherine']][:10])

    data['Berri 1'].plot()
    plt.show()
#
# articl_1()
def articl_2():
    print(data[:5])
    #выбор несколько колонок
    print(data[['Berri 1', 'Brabeuf (donnes non disponibles)', 'Cute-Sainte-Catherine']][:10])
    print(data['Berri 1'].value_counts())


# articl_2()
def articl_3():
    beri_bikes = data[['Berri 1']].copy()
    print(beri_bikes)
    print(beri_bikes.index)
    print(beri_bikes.index.day)
    beri_bikes.loc[:, 'weekday'] = beri_bikes.index.weekday
    print(beri_bikes[:8])
    week_count = beri_bikes.groupby('weekday').sum()
    week_count.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(week_count)
    week_count.plot(kind='bar')
    plt.show()
articl_3()
