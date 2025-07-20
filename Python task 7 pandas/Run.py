import pandas as pd
df=pd.read_csv('C:\\Users\\HP\Desktop\\Python task\\Employee.csv')
print(df.iloc[1:4])
print(df[["Name","Marks"]])
print(df.loc[df['Grade'] == 'A'])
