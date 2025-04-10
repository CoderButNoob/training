def find_product(lst , target):
    seen = set()
    for x in lst :
        if x!= 0 and target%x == 0 :
            if n//x in seen :
                return sorted([x , n//x])
        seen.add(x)
    
    return None

n = int(input("Enter size "))
target = int(input("Enter Target "))
lst = [int(input()) for _ in range(n)]
print(find_product(lst, target))
