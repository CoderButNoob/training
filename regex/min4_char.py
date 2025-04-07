import re
def valid(name):
    if re.match(r"^[a-zA-Z]{4}$",name):
        return "True"
    else:
        return "False"


name = input()
print(valid(name))