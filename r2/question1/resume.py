import re
import json
from faker import Faker


input_file = r"C:\Program Files\GE\training\r2\resume.json"
output_file = r"C:\Program Files\GE\training\r2\shortlist.json"
keyword = {"python" , "docker"}
email_pattern = re.compile(r"[\w\.-]+@[\w\.-]+\.\w{2,}")
with open(input_file,"r") as input:
     resumes = json.load(input)

shortlisted = []
for resume in resumes:
    name =  resume.get("name")
    email =  resume.get("email")
    content =  resume.get("content").lower()

    if email_pattern.match(email):
        matched = {k for k in keyword if k in content}
        if matched == keyword:
            shortlisted.append({"name":name, "email":email , "keyword":list(matched)})

with open(output_file,"w") as output:
    json.dump(shortlisted,output,indent=4)
    
