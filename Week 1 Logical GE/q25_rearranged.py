def diff(num):
    nums = list(str(num))
    maxi = int(''.join(sorted(nums , reverse=True)))
    mini = int(''.join(sorted(nums)))
    return maxi-mini 
num = int(input())
print(diff(num))