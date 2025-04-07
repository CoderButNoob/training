import re

def valid_email(email):
    if not re.match(r"^[^@]+@[^@]+$",email):
        return "Invalid : Email should have exactly one @"

    local , domain = email.split('@')

    if re.match(r"^\." , local) or re.match(r"$\.", local) :
        return "Invalid : Email should not start or end with '.'"
    
    if re.match(r"\.\.",email):
        return "Invalid : Email cant have '..' "
    
    if not re.match(r"^[\w\.-]+$",local):
        return "Invalid : Local part contains invalid chars"
    
    if not re.match(r"^[a-zA-Z]+\.[a-zA-Z]{2,}(?:\.[a-zA-z]{2,})*$",domain):
        return "Invalid : Domain name or TLD invalid"
    
    return "Valid"
    

    

email = input()
print(valid_email(email))