def missing_in_string(s):
    s = s.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    res = ''

    for i in alpha :
        if i not in s:
            res += i
    
    return res



s = input()
print(missing_in_string(s))