#1. 

import array as arr

num = arr.array('i',[])

for  i in range(5):
    a =  int(input())
    num.append(a)


for i in range(5):
    print(f"{i} ->",num[i])


#2.
import array as arr

def  count_occurance(arr,element):
    return arr.count(element)

    

num = arr.array('i',[])

for i in range(10):
    a = int(input())
    num.append(a)

element = int(input("Enter the element"))

occurance = count_occurance(num , element)

print(occurance)

#3. 
import array as arr

num = arr.array('i',[1,2,3,4,2,5,6])
element = 2
num.remove(element)
print(num.tolist())

#4.
import array as arr

def reverse(arr):
    arr.reverse()
    return arr


num = arr.array('i',[])

for i in range(5):
    a= int(input())
    num.append(a)

reverse_array = reverse(num)

print(reverse_array)


