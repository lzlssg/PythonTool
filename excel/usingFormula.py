# -*- coding: utf-8 -*-
from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook('sample.xlsx')
ws1=wb.active

ws1["A1"]=1
ws1["A2"]=2
ws1["A3"]=3

ws1["A4"] = "=SUM(1, 1)"
ws1["A5"] = "=SUM(A1:A3)"

print (ws1["A4"].value)  #打印的是公式内容，不是公式计算后的值,程序无法取到计算后的值
print (ws1["A5"].value)  #打印的是公式内容，不是公式计算后的值,程序无法取到计算后的值

# Save the file
wb.save("sample.xlsx")
