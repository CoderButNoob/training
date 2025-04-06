import  sys 

if len(sys.argv)<3:
    print("Useage : python practice.py name age")
else :
    name = sys.argv[1]
    age = sys.argv[2]
    print(f"{name} , {age}")
