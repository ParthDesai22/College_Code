import pandas as pd 

df = pd.read_csv('/home/admin1/Desktop/Data.csv')
#df = pd.read_excel("Data.ods", engine="odf")
des_values = df.describe()
#print(des_values,"/n")
#print(df.dtypes)
nan_count = df.isna().sum()
#print("/n",nan_count)
#print(df.info())
#print(df.shape)
#print(df.info)

#replacing null values with mean
mean = df['Europe'].mean().round(2)
print('Mean = ',mean)
df['Europe'] = df['Europe'].replace(0,mean)
for i in range (934,955):
    print(df['Europe'].iloc[i].round(2))

#replacing null values with mean
median = df['Japan'].median().round(2)
print('Median = ',median)
df['Japan'] = df['Japan'].replace(0,median)
for i in range (934,955):
    print(df['Japan'].iloc[i].round(2))

#replacing null values with mean
mode = df['Europe'].mode().round(2)
print('Mode = ',mode)
df['Rest of World'] = df['Rest of World'].replace(0,mean)
for i in range (934,955):
    print(df['Rest of World'].iloc[i].round(2))

#Last Observation Carried Forward
#for i in range (934,955):
#    df['Japan'].replace(to_replace=0,method='ffill').values
#for i in range (934,955):    
#    print(df['Japan'].iloc[i].round(2))
