#1. Write a Python program to create a set.
new_set = {'apple','banana','orange'}
print(new_set)

#2. Write a Python program to iteration over sets.
new_set = {'apple','banana','orange'}
for x in new_set:
    print(x)

#3. Write a Python program to add member(s) in a set.
new_set = {'apple','banana','orange'}
new_set.add('kiwi')
print(new_set)

#4. Write a Python program to remove item(s) from set
new_set = {'apple','banana','orange'}
new_set.remove('apple')

print(new_set)

#5. Write a Python program to remove an item from a set if it is present in the set.
new_set = {'apple','banana','orange'}
if('apple' in new_set):
    new_set.remove('apple')
print(new_set)

#6. Write a Python program to create an intersection of sets.
new_set1 = {'apple','banana','orange'}
new_set2 = {'apple','banana','orange','kiwi','papaya'}

updated_set = new_set1 & new_set2
print(updated_set)

#7. Write a Python program to create a union of sets.
new_set1 = {'apple','banana','orange'}
new_set2 = {'apple','banana','orange','kiwi','papaya'}
updated_set = new_set1 | new_set2
print(updated_set)

#8. Write a Python program to create set difference.
new_set1 = {'apple','banana','orange'}
new_set2 = {'apple','banana','orange','kiwi','papaya'}
updated_set = new_set2 - new_set1
print(updated_set)

#9. Write a Python program to create a symmetric difference.
new_set1 = {'apple','banana','orange'}
new_set2 = {'apple','banana','orange','kiwi','papaya'}
updated_set = new_set1.symmetric_difference(new_set2)
print(updated_set)

#10. Write a Python program to clear a set.

new_set1 = {'apple','banana','orange'}
new_set2 = {'apple','banana','orange','kiwi','papaya'}
updated_set = new_set1.clear()
print(updated_set)

#11. Write a Python program to use of frozensets.
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

#12. Write a Python program to find maximum and the minimum value in a set.
myset = {1,2,3,5,0,6}
maxi = max(myset)
mini = min(myset)
print(maxi,mini)









