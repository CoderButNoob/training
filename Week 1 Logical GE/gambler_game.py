import random 

def gamble(stake , goal , number_of_time):
    total_bet = 0
    win = 0


    for _ in range(number_of_time):
        cash = stake 
        bets = 0

        while 0 < cash < goal:
            bets += 1

            if random.random()<0.50:
                cash += 1
            else :
                cash -= 1
        
        total_bet += bets

        if cash == goal :
            win+=1
    
    win_percentage = (win/number_of_time)*100
    loss_percentage = 100 - win_percentage


    print(f"Number of wins:-{win}")
    print(f"Win % - {win_percentage}")
    print(f"Loose % -{loss_percentage}")

stake = int(input("Enter Amount-"))
goal = int(input("Enter Goal-"))
no_of_Trials = int(input("Number of Stimulations-"))

gamble(stake,goal,no_of_Trials)