with open(r"C:\Program Files\GE\training\file_handling2\q2\input.txt","r") as input:
    texts = input.read()
with open(r"C:\Program Files\GE\training\file_handling2\q2\output.txt","w") as output:
    for text in reversed(texts):
        output.write(text)
