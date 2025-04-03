def list_of_multiple(n,l):
    return [n*(i+1) for i in range(l) ]

n = int(input("Enter Number"))
l = int(input("Enter Length"))
print(list_of_multiple(n,l))