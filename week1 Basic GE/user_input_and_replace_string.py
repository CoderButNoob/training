def greeting(name):
    """ 
    This function takes input of user's name (mix 3 char) and returns output in greeting
    
    Args:
        name(str): user name input
    
    Reurns:
        String : A greeting with user name
        
    """
    #check the length of user name 
    if len(name)<3:
        return "Invlaid  Input"
    else :
        return f"Hello {name}, How are you"

name = input("Enter user name-")
print(greeting(name))
