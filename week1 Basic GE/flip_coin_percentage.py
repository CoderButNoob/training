import random

def find_coin_flip_percentage(num_of_flips):
    """
    Take input of Number of flips and calculate the percentage of head and tails

    Args :
        num_of_flips(int) : Number of times a coin is flippd
    
    Returns:
        int : Percentage value of Head occurance v/s Tail occurance
    """
    
    if num_of_flips<=0:
        print("Enter a positive number")
        return 
    
    #initialize head and tails 
    head = 0
    tails = 0

    #count the number of heads and tails
    for _ in range(num_of_flips):
        if random.random()<0.5:
            tails += 1
        else:
            head += 1
    
    #find the precentage 
    head_percentage = (head/num_of_flips)*100
    tails_percentage = (tails/num_of_flips)*100

    print(f"Total flips :{num_of_flips}")
    print(f"Heads: {head} ({head_percentage:.2f})%")
    print(f"Tails: {tails} ({tails_percentage:.2f})%")

flips =  int(input("Enter the number of Flips"))
find_coin_flip_percentage(flips)



