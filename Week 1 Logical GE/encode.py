def encode(s):
    c = 1 
    ch = s[0]
    res = ""

    for i in range(1,len(s)):
        if ch == s[i]:
            c+=1
        else:
            res += str(c) + ch
            c=1
            ch = s[i]
    
    print(res)
    



s = input()
encode(s)

