import heapq
#method 1 (normal sorting)
def find_k_smallest(list,n,k):
    list.sort()
    return list[k-1]


#method 2 (using heap)
def find_k_smallest(list,k):
    return heapq.nsmallest(k,list)[-1]

list = []
n = int(input("Enter Size"))
k = int(input("Enter value of K "))
for _ in range(n):
    a = int(input())
    list.append(a)

print(find_k_smallest(list,k))
