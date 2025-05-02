import re
import json
from collections import Counter

input_file = r"html.txt"
output_file = r"tag_count.json"

with open(input_file,"r") as input:
    content = input.read()

    html_pattern = re.compile(r"<\s*(\w+)")
    tags = html_pattern.findall(content.lower())

    tag_count = Counter(tags)

with open (output_file,"w") as output:
    json.dump(tag_count,output,indent=4)
