def find_common(list1,list2,list3):
    '''res =[]
    for x in list1:
        if x in list2 and x in list3:
            if x not in res:
                res.append(x)

    sum = 0 
    for x in res :
        sum += x
    
    print(sum)'''

    res = list(set([x for x in list1 if x in list2 and x in list3]))
    print(sum(res))
    

n = int(input())
list1  = [int(input("Enter Val for List1 ")) for _ in range(n)]
list2 = [int(input("Enter Val for List2 ")) for _ in range(n)]
list3 = [int(input("Enter Val for List3 ")) for _ in range(n)]
find_common(list1,list2,list3)