def calculate(num):
    total_sum = 0
    for digit in str(num):
        n = int(digit)
        total_sum += n**2
    return total_sum


def happy_number(num):
    seen = set()
    while num != 1:
        if num in seen :
            return False
        seen.add(num)
        num = calculate(num)
        
    return True


n =  int(input("Enter a number"))
print(happy_number(n))
