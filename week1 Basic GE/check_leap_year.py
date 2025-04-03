def leap_year_or_not(year):
    """
    Take Input as Year and Give the output if the year provided is leap year or not

    Args:
      year(int) : Year which is to be Evaluated as a Leap yer or not

    Returns:
       True/False : If the year is Leap Year or not.
    """

    if year <= 0:
        print("Invalid year !!")
        return
    
    if year % 4 ==0 :
        return True
    elif year % 100 ==0 :
        return False
    elif year % 400 ==0 :
        return True 
    else:
        return False


year =  int(input("Enter Year"))

if leap_year_or_not(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
