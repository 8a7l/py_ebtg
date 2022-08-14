import matplotlib.pyplot as plt
import numpy as np
import openpyxl
print('Автор: Василь Онуфрійчук') 
print('Parser елементів списку із файлу ексель.')
print('')
a=list()
b=list()
c=list()
table_name='You-table.XLSX'
def build_list(a,b,h):
    k=1
    for i in range(h):
        x=sheet_wb[b+str(k)].value
        a.append(x)
        k+=1
def getmess(a,b,c):
    ws = wb.active
    k=''
    r='\n'
    p=' '
    for i in range(len(a)):
       k+=a[i]+p*2+b[i]+p*3
    ws[c]=k    
    wb.save(table_name)


wb = openpyxl.load_workbook(table_name)
sheet_wb=wb.active
b_wb=sheet_wb['C1'].value
d_wb=sheet_wb['C1'].value
build_list(a,'A',b_wb)
build_list(b,'B',d_wb)


getmess(a,b,'D1')
