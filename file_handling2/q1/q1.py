#file1 = open(r"C:\Program Files\GE\training\file_handling2\q1\file1.txt","r")

with open(r"C:\Program Files\GE\training\file_handling2\q1\file1.txt","r") as input:
    text = input.read().lower()

words = text.split()

word_count = {word:words.count(word) for word in set(words)}

with open(r"C:\Program Files\GE\training\file_handling2\q1\word_count.txt" , "w") as output:
    for word , count in sorted(word_count.items()):
        output.write(f"{word}:{count}\n")
    


