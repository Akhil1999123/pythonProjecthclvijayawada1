import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook('C:\pythonProjecthclvijayawada\dataset\Book1.xlsx')
sheet=wb.active
sheet["A7"]='=SUM(A1:A6)'
wb.save('C:\pythonProjecthclvijayawada\dataset\Book1.xlsx')