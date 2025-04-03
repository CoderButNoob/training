def find_factors(num):
    """
    This Function finds the factors of a number

    Args:
        num(int) - Number to find the factor of
    
    Returns:
        list : A list of Prime Factors
    """

    if num < 0 :
        raise ValueError("Enter a Positive Number")
    
    factors = []
    i  = 2
    while i*i < num:
        if num%i != 0:
            i+=1
        else:
            num//=i
            if i  not in factors:
                factors.append(i)
    
    if num  > 1:
        if num not in factors:
            factors.append(num)
    

    return factors



num = int(input("Enter a number"))
factors = find_factors(num)
print(f"The prime factors of {num} are : {factors}")

