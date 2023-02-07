from openpyxl import load_workbook
from openpyxl.drawing.image import Image

workbook =load_workbook(filename="C:\pythonProjecthclvijayawada\dataset\Book2.xlsx")
sheet =workbook.active

logo=Image("C:\pythonProjecthclvijayawada\dataset\spy.jfif")
logo.height =150
logo.width = 150

sheet.add_image(logo,"D10")
workbook.save("C:\pythonProjecthclvijayawada\dataset\Book1.xlsx")