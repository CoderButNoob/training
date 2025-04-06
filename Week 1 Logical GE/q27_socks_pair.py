from collections import Counter
def find_pair(lst):
    color_count = Counter(lst)
    pairs = sum(count // 2 for count in color_count.values())
    return pairs

    return d
n = int(input())
lst = [int(input()) for _ in range(n)]
print("No of Pairs = ",find_pair(lst))
