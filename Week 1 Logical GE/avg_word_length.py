#3.For a given sentence, return the average word length.
import string
def avg_length(str_no):
    str_no = str_no.translate(str.maketrans('','',string.punctuation))
    
    words = str_no.split()
    
    
    if not words:
        return 0
    
    total_len = 0
    
    for word in words:
        total_len += len(word)
    
    avg_len = total_len/len(words)

    return avg_len




s = input("Enter string")
print(avg_length(s))

