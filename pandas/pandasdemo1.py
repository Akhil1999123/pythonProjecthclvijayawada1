import pandas as pd
d={"Team":["India","australia","pakistan","srilanka","england"], "rank":[1,2,3,4,5],
   "winner":["60%","50%","45%","35%","48%"]
   }
df=pd.DataFrame(d)
#df.rename(columns={"rank":"Ranking"},inplace=True)
#df.set_axis(df['Team'],inplace=True)
#rint(df.loc[df['Ranking']>=3])
print(df)
#f.drop([0,3],axis=0,inplace=True)
df.drop(['winner'],axis=1,inplace=True)
print(df)