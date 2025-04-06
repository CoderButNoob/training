def sort_pos(lst):
    pos_lst = sorted([x for x  in lst if x>=0])
    return [x if x < 0  else pos_lst.pop(0) for x in lst]


n = int(input("Enter size "))
lst = [int(input()) for _ in range(n)]
print(sort_pos(lst))