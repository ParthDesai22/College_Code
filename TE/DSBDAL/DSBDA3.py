import pandas as pd 

df = pd.read_csv('/home/admin1/Desktop/Data.csv')
des_values = df.describe()
print(des_values,"/n")
print(df.dtypes)
nan_count = df.isna().sum()
print("/n",nan_count)