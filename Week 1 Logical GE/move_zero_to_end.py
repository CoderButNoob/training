#Method 1
def move_zero(list,n):
    dummy = []
    count_zeros = 0
    for num in list :
        if num != 0 :
            dummy.append(num)
        else:
            count_zeros+=1
    dummy.extend([0]*count_zeros)
    return dummy

#method 2 (optimized)
def move_zero(list,n):
    l = 0 
    for r in range(len(list)):
        if list[r]!=0:
            list[l],list[r]=list[r],list[l]
            l+=1


list = []
n = int(input("Enter size "))
for _ in range(n):
    a = int(input())
    list.append(a)
move_zero(list,n)
print(list)
