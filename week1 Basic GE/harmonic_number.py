def harmonic_number(n):
    """
    Prints the nth harmonic number 

    Args:
        n(int) : number of terms in harmonic series

    Return: 
        float - The nth harmonnic number 
    """

    if n <= 0 :
        print("Invlaid")
        return 
    
    harmonic_sum = 0.0

    for i in range(1,n+1):
        harmonic_sum += 1/i
    
    return round(harmonic_sum,4)



num = int(input("Enter a Number"))
print(f"The Nth Harmonic Number is :{harmonic_number(num)}")
