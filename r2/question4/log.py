import re
import json
from collections import Counter
input_file = r"log.txt"
output_file = r"log.json"
d = {} 
with open(input_file,"r") as input:
    contents = input.readlines()
    for line in contents:
        email = re.search(r"[\w\.-]+@[\w\.-]+\.\w{2,}",line)
        user_match =  re.search(r"user\s+(\w+)",line)
        user = email.group() if email else user_match.group(1) if user_match else None
        ip_add = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",line)
        ip = ip_add.group() if ip_add else None

        if user:
            if user not in d:
                d[user]={"count":0, "ip":[]}
            d[user]["count"] += 1
            if ip and ip not in d[user]["ip"]:
                d[user]["ip"].append(ip)

with open(output_file,"w") as output:
    json.dump(d,output,indent=4)