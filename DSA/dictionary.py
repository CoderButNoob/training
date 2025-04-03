#Dictionary
#1. Write a Python script to sort (ascending and descending) a dictionary by value.
d = {'a':1,'b':4,'c':3,'d':0,'e':6,'f':5}

d_asc = sorted(d.items(),key=lambda x:x[1])
print(d_asc)

d_des = sorted(d.items(),key= lambda x:x[1],reverse=True)
print(d_des)

#2. Write a Python script to add a key to a dictionary.
d = {0: 10, 1: 20}
d[2]=30
print(d)

#3. Write a Python script to concatenate following dictionaries to create a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = dic1 | dic2 | dic3
print(dic4)


#4. Write a Python program to iterate over dictionaries using for loops.
d = {'a':1,'b':4,'c':3,'d':0,'e':6,'f':5}
for k,v in d.items():
    print(k)
    print(v)

#5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = int(input())
new_dict = {x:x*x for x in range(1,n+1)}
print(new_dict)

#6. Write a Python program to remove a key from a dictionary.
d = {'a':1,'b':4,'c':3,'d':0,'e':6,'f':5}
d.pop('a')
print(d)

#7. Write a Python program to print all unique values in a dictionary.
d= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique = set() #set to  add only unique value

for items in d:
    for value in items.values():
        unique.add(value)

print(unique)

#8. Write a Python program to create a dictionary from a string.
string = 'w3resource'
d={}
for char in string:
    d[char]=d.get(char,0)+1
print(d)

#10. Write a Python program to count the values associated with key in a dictionary.

data= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['success'] for  d in data))

#13. Write a Python program to count number of items in a dictionary value that is a list.
d = {   'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'B' : 34,
        'C' : 12,
        'D' : [7, 8, 9, 6, 4] }
count = 0
for x in d :
    if isinstance(d[x],list):
        count+=1
print(count)

#12.  Write a Python program to check multiple keys exists in a dictionary.
d = {'a':1,'b':4,'c':3,'d':0,'e':6,'f':5}
l=len(d)
if l > 1:
    print("Multiple present")
else:
    print("No multiple")

#11. Write a Python program to convert a list into a nested dictionary of keys.
a = ['gfg','is','best']
b = ['I','learn','python']
c = [1,2,3]
d = {}
for i,j,k in zip(a,b,c):
    d[i]={j:k}
print(d)

#9. Write a Python program to print a dictionary in table format.
d = {1: ["Samuel", 21, 'Data Structures'],
         2: ["Richie", 20, 'Machine Learning'],
         3: ["Lauren", 21, 'OOPS with java'],
         }

print("{:<10} {:<10} {:<10}".format('Name','age','course'))

for key,value in d.items():
    name,age,course = value
    print("{:<10} {:<10} {:<10}".format(name,age,course ))


