def swap_vowel(vowel,string):
    string = list(string)
    j = len(vowel)-1
    i = 0
    while i < j:
        if string[i]in vowel and string[j] in vowel :
            string[i],string[j]=string[j],string[i]
            j -= 1
            i += 1
        elif string[i] not in vowel:
            i += 1
        elif string[j] not in vowel:
            j -= 1
        
    print ("".join(string))  
        
vowel = ['a','e','i','o','u','A',"E","I",'O','U']
string = "ALex is A Cheater"
swap_vowel(vowel,string)
