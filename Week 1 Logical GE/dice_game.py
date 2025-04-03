import random
def dice_game(store):
    score = 0
    print(store)
    for a,b in store:
        if a==b :
            return 0
        
        score+=a+b
    
    return score


store =  []
for _ in range(3):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)

    store.append((roll1,roll2))

print(dice_game(store))
