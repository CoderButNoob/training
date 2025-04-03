def alphabet_idx(alphabet,string):
    max_idx = -1
    max_ele = ''

    for char in string:
        if char in alphabet:
            idx = alphabet.index(char)+1
            if idx > max_idx:
                max_idx = idx
                max_ele = char
    
    print(f"{max_idx}{max_ele}")




alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
"v", "w", "x", "y", "z"]
string = input("Enter String")
alphabet_idx(alphabet,string)