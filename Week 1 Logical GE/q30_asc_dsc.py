def asc_dsc_none(lst,s):
    if s == 'ASC':
        print(sorted(lst))
    elif s ==  'DSC':
        print(sorted(lst,revese = True))
    elif s== 'NONE':
        print(lst)
    else:
        print("Invalid !!")



n =  int(input("Enter size : "))
lst = [int(input()) for _ in range(n)]
s = input("Enter ASC/DSC/NONE : ")
asc_dsc_none(lst,s)