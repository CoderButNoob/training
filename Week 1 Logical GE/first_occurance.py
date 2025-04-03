def find_occurance(text , pattern):
    return text.find(pattern)

text = input("Enter text")
pattern = input("Enter Pattern")

print(find_occurance(text , pattern))
