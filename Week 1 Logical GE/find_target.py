import array as arr
def find_target(nums, target):
   ''' d = {}
    for i , num in enumerate(nums):
        compliment = target - num 
        if compliment in d :
            return[d[compliment],i]
        d[num]=i
    
    return []'''
   


n = int(input("Enter desired length"))
target = int(input("Enter target"))
a = arr.array('i',[])
for i in range(n):
    num = int(input())
    a.append(num)

result = find_target(a,target)
print(result)
