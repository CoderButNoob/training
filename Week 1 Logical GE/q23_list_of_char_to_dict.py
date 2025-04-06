def to_dict(lst):
    return [{ch : ord(ch)} for ch in lst]

n = int(input())
lst = [input() for _ in range(n)]
print(to_dict(lst))
