import pandas as pd
import numpy as np
data1=pd.read_excel('..//dataset//Book3.xlsx',sheet_name="Sheet1")
data2=pd.read_excel('..//dataset//Book3.xlsx',sheet_name="Sheet2")
print(data1)
print(data2)
data3=np.where(data1['s.n2']==data2['name'],True,data2['s.n2']-data1['name'])
print(data3)