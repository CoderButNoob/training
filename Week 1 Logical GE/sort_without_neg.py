def sort(lst):
    pos_num = sorted([num for num in lst if num > 0])
    pos = iter(pos_num)
    return [next(pos) if num > 0 else num for num in lst]

n = int(input())
lst = [int(input())for _ in range(n)]
print(sort(lst))