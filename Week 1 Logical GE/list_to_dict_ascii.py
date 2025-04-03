def to_dict(list):
    return [{char : ord(char)} for char in list]
n = int(input())
list = [input() for _ in range(n)]
print(to_dict(list))
 