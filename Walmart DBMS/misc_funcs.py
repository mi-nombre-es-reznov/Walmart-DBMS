# v.1.1.1 - Nicholas Perez-Aguilar
'''

'''
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

def Menu(Men_ops):
    tot_opts = len(Men_ops)
    usr_choice = 0
    
    # Display menu
    print("\t\t\tMenu\n\n\n")
    for i in range(len(Men_ops)):
        print(str(i + 1) + ") " + Men_ops[i])
        
    # Allow choice from available options
    try:
        while(usr_choice > tot_opts or usr_choice < 1):
            usr_choice = int(input("\nPlease select an option: "))
    except ValueError:
        print("Please enter a number!\n\n")
        usr_choice = 0
        Menu(Men_ops)
    
    return usr_choice

def space():
    for i in range(10):
        print("\n")

#print(time_mil_to_civ_hr(700))
#print(time_mil_to_civ_hr(900))
#print(time_mil_to_civ_hr(1200))
#print(time_mil_to_civ_hr(1900))