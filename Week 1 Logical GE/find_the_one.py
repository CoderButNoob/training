#5. Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
def find_the_one(list , n):
    d={}
    for num in list:
        d[num] =  d.get(num,0)+1
    for key,count in d.items():
        if count == 1:
            return key
    
    return None


list = []
n = int(input("Enter list size"))
for _ in range(n):
    a = int(input())
    list.append(a)

unique = find_the_one(list,n)
print(unique)
