
m openpyxl import Workbook
wb = Workbook()

ws1 = wb.create_sheet("Mysheet")           #创建一个sheet
ws1.title = "New Title"                    #设定一个sheet的名字
ws2 = wb.create_sheet("Mysheet", 0)      #设定sheet的插入位置 默认插在后面
ws2.title = u"你好"    #设定一个sheet的名字 必须是Unicode

ws1.sheet_properties.tabColor = "1072BA"   #设定sheet的标签的背景颜色

#获取某个sheet对象
print wb.get_sheet_by_name(u"你好"  )
print wb["New Title" ]

#获取全部sheet 的名字，遍历sheet名字
print wb.sheetnames
for sheet_name in wb.sheetnames:
		    print sheet_name

			print "*"*50

			for sheet in wb:
					    print sheet.title

#复制一个sheet
wb["New Title" ]["A1"]="zeke"
source = wb["New Title" ]
target = wb.copy_worksheet(source)

# w3 = wb.copy_worksheet(wb['new title'])
# ws3.title = 'new2'
# wb.copy_worksheet(wb['new title']).title = 'hello'
# Save the file
wb.save("\sample.xlsx")i
