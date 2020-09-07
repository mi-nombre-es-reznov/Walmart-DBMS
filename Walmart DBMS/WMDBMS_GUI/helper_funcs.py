# import only system from os
from os import system, name

# define our clear function
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def continues():
    '''
    c -- String: User input
    '''
    c = ""
    
    while(c != "y"):
        c = input("Continue? [y]: ")
        
        # Convert to lower
        c = c.lower()
        
def time_conv_hr(mil):
    civ = 0
    append = ":00:00"
    final_time = ""

    civ = (mil / 100) # Time less than 24

    if(civ == 12):
        final_time = "12:00:00"
    else:
        civ = int(civ)
        final_time = (str(civ) + append)
        
    return final_time