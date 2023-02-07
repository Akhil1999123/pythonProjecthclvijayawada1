from openpyxl import Workbook
from openpyxl.chart import BarChart,Reference,PieChart
wb=Workbook()
sheet=wb.active
sales_data=[["years","sales"],
           [2000,30],
           [2001,49],
           [2002,50],
           [2003,80],
           [2004,70],
           [2005,80],
           [2006,30]
           ]
for row in sales_data:
    sheet.append(row)
chart=PieChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"C1")
wb.save("C:\pythonProjecthclvijayawada\dataset\Book3.xlsx")