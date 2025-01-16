import pandas as pd

df=pd.read_csv('/home/bibek/Desktop/python1/pandas_pd/cleaning_pd/data.csv')

# df.dropna(inplace = True)
# df.fillna(123,inplace=True)
# df["Calories"].fillna(123,inplace=True)
# x=df["Calories"].mean()
# df["Calories"].fillna(x,inplace=True)
# print(df)
# print(x)
df['Date'] = pd.to_datetime(df['Date'],format='mixed', errors='coerce')

# df.loc[7,'Duration']=45
# print(df.to_string())

# for x in df.index:
  
#   if df.loc[x, "Duration"] ==120:
#     df.loc[x, "Duration"] = 120

# for x in df.index:
#   if df.loc[x,"Duration"]>120:
#     df.drop(x,inplace=True)
# print(df.to_string())
df.duplicated()
df.drop_duplicates(inplace=True)
print(df.to_string())

