import pandas as pd
import numpy as np
df=pd.read_csv("..//dataset//tested.csv")   #loading the dataset in pycharm
print(df)
#print(df.shape)
#print(df.isna().any)
df.drop(['Cabin'],axis=1,inplace=True)
df.fillna(method='ffill',inplace=True)
print(df['Embarked'])
#print(df.isna().sum())
#print(pd.crosstab(index=df['PassengerId'],columns=df['Survived']))
#print(df.groupby(['Sex','Survived'])['Survived'].count())
#print(df.describe())
print(pd.crosstab(index=df['Sex'],columns=df['Survived']))
print(pd.pivot_table(df,index=['Sex','Age'],aggfunc=np.sum))
print(df.sort_values(by=['Pclass','Age'],ascending=False))
df['Survived']=df['Survived'].apply(lambda val:'Yes' if val==1 else 'No')
print(df)