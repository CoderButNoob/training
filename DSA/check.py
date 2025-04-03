d = {   'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B' : 34,
        'C' : 12,
        'D' : [7, 8, 9, 6, 4] }
count = 0
for x in d :
    if isinstance(d[x],list):
        count+=1
print(count)