def lottery(lst):
    sublist = lst[0]
    win = lst[1]
    mini_win = 0 
    for sublist in ticket:
        code , num = sublist
        if any(ord(ch) == num for ch in code):
            mini_win+=1
    
    if mini_win >= win:
        print("Winner")
    else:
        print("Looser")

ticket = []
n = int(input("Enter size"))
for _ in range(n):
    code = input("Enter Code")
    val = int(input("Enter Value"))
    ticket.append([code,val])
win = int(input("Enter Win Condition"))
lst = [ticket,win]
lottery(lst)

