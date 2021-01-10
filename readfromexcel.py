import xlrd

loc = ("C:\\Users\\hp\\Desktop\\GUVI_Python\\Book1.xls")

wb = xlrd.open_workbook(loc)

sheet1 = wb.sheet_by_index(0)
sheet2 = wb.sheet_by_index(1)

print(sheet1.cell_value(3,3))
print(sheet2.cell_value(0,1))

print(sheet1.ncols)
print(sheet2.ncols)

print(sheet1.nrows)
print(sheet2.nrows)

for i in range(sheet1.ncols):
    print(sheet1.cell_value(i,0))

print(sheet1.row_values(1))
print(sheet1.col_values(1))