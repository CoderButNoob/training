def find_target(list, target):
    d = {}
    for i in range(len(list)):
        d[list[i]]=i
    
    return d.get(target,-1)


list = []
n = int(input("Enter size ="))
target = int(input("Enter Target Value ="))
for _ in range(n):
    a = int(input())
    list.append(a)

print("Index= " ,find_target(list,target))


