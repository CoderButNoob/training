#8.Given a positive number, check if it is a perfect square without using any built-in library function.
#using loop 
#method 1
def perfect_square(num):
    if num == 1:
        return True
    
    for i in range(1,int(num**0.5)+1):
        if i*i == num:
            return True
    return False

n = int(input("enter a number"))
print(perfect_square(n))



#using binary search
#method 2
def perfect_square(num):
    if num < 0:
        return False
    left , right = 0, num

    while left < right :
        mid = (left+right)//2

        if mid*mid == num:
            return True 
        elif mid*mid < num:
            left = left+1
        elif mid* mid > num:
            right = mid -1 
    
    return False




n = int(input("enter a number"))
print(perfect_square(n))

