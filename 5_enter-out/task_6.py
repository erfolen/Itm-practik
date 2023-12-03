import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt

work_dir = Path.cwd()
data_path = Path(work_dir, 'dataset', 'bikes.csv')

data = pd.read_csv(data_path)

print(data.head(10))


#task 7
print(sum(data['Rachel1']))
