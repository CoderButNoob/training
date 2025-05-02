def is_suffled(lst):
    return not any(
        all(lst[i+j]-lst[i+j]==d for j in range(1,3))
        for i in range(len(lst)-2)
        for  d in (1,-1)
    )
n = int(input())
lst = [int(input()) for _ in range(n)]
print(is_suffled(lst))
