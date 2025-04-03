def reverse_arr(nums):
    left = 0 
    right = len(nums)-1

    while left <= right :
        nums[left],nums[right]=nums[right],nums[left]
        left += 1
        right -= 1
    
        


n = int(input("Enter size: "))
nums = []
for _ in range(n):
    a = int(input())
    nums.append(a)
reverse_arr(nums)
print(nums)