import pandas as pd

df = pd.read_csv('/home/bibek/Desktop/python1/pandas_pd/correlations/data.csv')

print(df.corr())