def excel_col_num(columnTitle : str)->int:
    res = 0 
    for ch in columnTitle:
        res = res*26 +  (ord(ch)-ord('A')+1)
    return res 

print(excel_col_num("AA"))