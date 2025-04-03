#6.Given an array nums of size n, return the majority element.
def find_majority(nums,n):
    d = {}
    for num in nums:
        d[num]= d.get(num,0)+1

    max_freq = 0
    max_elemnt = 0
    for key,value in d.items():
        if value > max_freq:
            max_freq = value
            max_elemnt = key
    return max_elemnt



n = int(input("Enter size "))
nums = []
for _ in range(n):
    a= int(input())
    nums.append(a)

print(find_majority(nums,n))
