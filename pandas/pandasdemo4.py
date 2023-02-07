import pandas as pd
d1= {'Name':['Pankaj','Megana','Lisa'],
    'country' :['india','india','USA'],
    'Role':['CEO','CTO, 'CEO'] }
df1 =pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame({'Id:[1,2,3],'Name' :['Pankaj','Anupam','Amit']})
print(df2)
df_merged =df1.merge(df2,how='right',on=df2['ID'])
print(df_merged)