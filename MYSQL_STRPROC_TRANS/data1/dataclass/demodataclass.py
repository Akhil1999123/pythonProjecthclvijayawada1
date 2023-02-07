from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass
class people():
    name:str
    no:int
    age:int
p=[people("akhil",1,25),people("suresh",2,25),people("avinash",3,20)]
data=[[p.name,p.no,p.age]for p in p]
data=[['Name','Num','Age']]+data


for d in data:
    sheet.append(d)
wb.save("C:\pythonProjecthclvijayawada\dataset\Book1.xlsx")