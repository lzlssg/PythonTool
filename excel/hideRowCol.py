# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

wb = load_workbook('sample.xlsx')
ws1=wb.active

ws1.column_dimensions.group('A', 'D', hidden=False)   #隐藏a到d列范围内的列
ws1.row_dimensions.group(1, 4, hidden=True)           #隐藏1到4行范围内的行
# Save the file
wb.save("sample.xlsx")
