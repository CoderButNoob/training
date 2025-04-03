#LIST
#1. Write a Python program to sum all the items in a list.
list = [1,2,3,4,5]
sum =  0
for item in list:
    sum+=item
print(sum)

#2. Write a Python program to multiplies all the items in a list.
list = [2,3,4]
mul = 1
for item in list:
    mul = mul*item
print(mul)

#3. Write a Python program to get the smallest number from a list.
list = [1,2,3]
mini = min(list)
print(mini)

#4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
list = ['abc', 'xyz', 'aba', '1221']
count=0
for item in list:
    if len(item)>=2 and item[0]==item[-1]:
        count+=1
print(count)

#5. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def get_last_ele(tup):
    return tup[-1]

list.sort(key=get_last_ele)

print(list)

#6. Write a Python program to remove duplicates from a list.
list = [1,2,3,4,2,3,1]
unique =  []

for item in list :
    if item not in unique:
        unique.append(item)

print(unique)

#7. Write a Python program to clone or copy a list.
list = [1,2,3,4,2,3,1]
mylist = list.copy()
print(mylist)

#8. Write a Python program to find the list of words that are longer than n from a given list of words.
list = ['Hello','Aniket','Doggy','Students','Apple']
n = 6
new_list = []
for items in list:
    if len(items) > n:
        new_list.append(items)

print(new_list)

#9. Write a Python function that takes two lists and returns True if they have at least one common member.
list1 = [1,2,3,42,5,6]
list2 = [42,53,66,2,4,6]
flag = False

for items in list1:
    if items in list2:
        flag = True
        break

print(flag)

#10. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
index = [0,4,5]
for i in sorted(index,reverse=True):
    list.pop(i)
print(list)


#11. Write a Python program to generate all permutations of a list in Python.
from itertools import permutations

my_list = [1,2,3]
permuations_list = list(permutations(my_list))
print(permuations_list)

#12. Write a Python program to get the difference between the two lists.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

diff = list(set(list1)-set(list2))

print(diff)

#13. Write a Python program to append a list to the second list.
#append
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

list1.append(list2)
print(list1)
#extend
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

list1.extend(list2)
print(list1)

#14. Write a python program to check whether two lists are circularly identical.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]

if len(list1) == len(list2):
    extended_list = list1 * 2 
    is_circularly_identical = any(list2 == extended_list[i:i+len(list2)] for i in range(len(list1)))
else:
    is_circularly_identical = False

print(is_circularly_identical)

#15. Write a Python program to find common items from two lists.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
common = []
for x in list1 :
    if x in list2:
        common.append(x)

print(common)

#16. Write a Python program to split a list based on first character of word.
words = ["apple", "banana", "apricot", "blueberry", "cherry", "carrot", "avocado"]
split_dict = {}

for  word in words:
    first_char = word[0]
    if first_char not in split_dict:
        split_dict[first_char]=[]
    split_dict[first_char].append(word)

for key , value in split_dict.items():
    print(f"{key} : {value}")

#17. Write a Python program to remove duplicates from a list of lists.
list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = []

for x in list:
    if x not in new_list:
        new_list.append(x)

print(new_list)