#1. Write a Python program to create a tuple.
t = (('apple','banana','guava'))
print(t)

#2. Write a Python program to create a tuple with different data types.
t = (('apple',True,3,1,'male'))
print(t)

#3. Write a Python program to unpack a tuple in several variables.
#method 1 using *
t = ('a','b','c','d','e')
(x,y,*z) = t
print(x)
print(y)
print(z)
#method 2 normal
t = ('a','b','c')
(x,y,z) = t
print(x)
print(y)
print(z)

#4. Write a Python program to create the colon of a tuple.
t = ('a','b','c')
cloned = t[:]
print(cloned)

#5. Write a Python program to find the repeated items of a tuple.
t = (1,2,3,1,4,1)
st = tuple(set(t))
print(st)

#6. Write a Python program to check whether an element exists within a tuple.
t = (1,2,3,1,4,1)
if 1 in t :
    print("yes")

#7. Write a Python program to convert a list to a tuple.
list = [4,5,6]
t = tuple(list)
print(t)

#8. Write a Python program to remove an item from a tuple.
t = ('a','b','c')
y = list(t)
y.remove('a')
t = tuple(y)
print(t)

#9. Write a Python program to slice a tuple.
t = (1,2,3,4,5,6)
print(t[1:4])
print(t[:4])
print(t[1:])

#10. Write a Python program to reverse a tuple.
t = (1,2,3,4,5,6)
r_t = t[::-1]
print(r_t)


