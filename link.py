import openpyxl

links = open(r'C:\Users\Asus1\Desktop\Links.txt','r',encoding='utf-8')
lks = links.readlines()

workbook = openpyxl.load_workbook(r'entertainment.xlsx')
sheet = workbook.get_sheet_by_name('Sheet1')
matched = []
for l in lks:
    for j in range(2,12):
        if sheet.cell(row=j,column=6).value in l :
            matched.append(l)
