import pandas as pd
import numpy as np
class Readcsv():
    def create_df(self,path):
        self.path=path
        self.df=pd.DataFrame(self.path)
        return self.df
    def total_df(self):
        self.df['Total']=self.df.iloc[:,2:],sum(axis=1)
        return self.df
    def avg_def(self):
        self.df['avg']=self.df['Total']/5
        return self.df
    def rank(self):
        
obj=Readcsv()
df=pd.read_csv("..//dataset//hcl.csv")
print(obj.create_df(df))
print(obj.total_df())
print(obj.avg_def())
"""
import pandas as pd
import numpy as np
df=pd.read_csv("..//dataset//hcl.csv")
#print(df)
df['Total']=df.iloc[:].sum(axis=1)
df['avg']=df['Total']/5
df['Rank']=df['avg'].rank()
#df['Result']=np.where((df['m1']>=35))
print(df.sort_values(by=['Rank']))
"""