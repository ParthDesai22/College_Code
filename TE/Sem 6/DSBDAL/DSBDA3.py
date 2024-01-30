import pandas as pd 

df = pd.read_csv('/home/admin1/Dataset/F21111022/Data.csv')
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
mean = df['Europe'].mean()
print('Mean = ',mean)
df['Europe'] = df['Europe'].replace(0,mean)
for i in range (934,955):
    print(df['Europe'].iloc[i].round(2))

#replacing null values with mean
median = df['Japan'].median()
print('Median = ',median)
df['Japan'] = df['Japan'].replace(0,median)
for i in range (934,955):
    print(df['Japan'].iloc[i].round(2))

#replacing null values with mode
mode = df['Europe'].mode()
print('Mode = ',mode)
df['Rest of World'] = df['Rest of World'].replace(0,mean)
for i in range (934,955):
    print(df['Rest of World'].iloc[i].round(2))

#Last Observation Carried Forward
#df['Japan'] = df['Japan'].fillna(method='ffill')
df['Japan']=df['Japan'].ffill()
for i in range (934,955):    
    print(df['Japan'].iloc[i])

#Next Observation Crarried Backward
#df['Japan']=df['Japan'].fillna(method='bfill')
df['Japan']=df['Japan'].bfill()
for i in range (934,955):    
    print(df['Japan'].iloc[i])
