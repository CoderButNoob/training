def calculate(num1,num2,num3):
    a =  num1%10
    b = num2%10
    c = num3%10

    if a*b == c:
        return True
    else:
        return False
num1 = int(input("Enter 1st Num"))
num2 = int(input("Enter 2st Num"))
num3 = int(input("Enter 3st Num"))
print(calculate(num1,num2,num3))
