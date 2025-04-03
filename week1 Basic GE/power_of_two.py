def print_power_of_2(num):
    """
    
    Take the Input as a Intergr which would compute the power 2
    Args: 
        num(int): Value between 0 to 30
        
    Returns
        Power of 2  upto num
    
    """

    if num <0 and num >= 31:
        print("Enter a number between 0 to 30")
        return
    
    for i in range(num+1):
        print(f"2^{i} = {2**i}")

num = int(input("Enter a power value between 0 to 30 -"))
print_power_of_2(num)


