def reverse_num(n):
    if n <  0 :
        reversed_num = -int(str(abs(n))[::-1])
    else:
        reversed_num = int(str(n)[::-1])
    return reversed_num

n = int(input("Enter num"))
reversed_num = reverse_num(n)
print(reversed_num)