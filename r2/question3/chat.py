import re
import json
input_file = r"chat.txt"
output_file = r"chat.json"
data = []
with  open(input_file,"r") as input , open(output_file,"w") as output:
    chats = input.readlines()
    for chat in chats:
        d = {}
        time = re.search(r"\[(\d{2}:\d{2})\]", chat)
        sender_match = re.search(r"\]\s*([A-Za-z]+)(?:\s*->\s*([A-Za-z]+))?:\s*(.*)", chat)
        

        if time and sender_match:
            d["time"] = time.group(1)
            d["sender"] = sender_match.group(1)
            d["message"] = sender_match.group(3)
            d["receiver"] = sender_match.group(2) if sender_match.group(2) else None
            data.append(d)
    json.dump(data,output,indent=4)