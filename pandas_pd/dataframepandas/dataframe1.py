import pandas as pd

df=pd.DataFrame(data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':["New York",'Los Angeles','Chicago'],
    'Salary': [70000, 80000, 90000]
      })
# print(df)
# print(df.head(1))

df.to_csv("/home/bibek/Desktop/python1/pandas_pd/dataframepandas/demo.csv",index=False)


# name=df['Name']
# print(name)
# subset=df[['Name','Age']]
# print(subset)

# sorted_df=df.sort_values(by='Age',ascending=True)
# print(sorted_df)

grouped_by=df.groupby('Age')[['Salary']].mean()
print(grouped_by)