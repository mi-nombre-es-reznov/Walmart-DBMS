# v.1.1.1 - Nicholas Perez-Aguilar
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
        
    
def get_y_n_choice(mess):
    choice = ""
    
    space()    
    while(choice != 'n' and choice != 'y'):
        choice = input(mess)
        
        choice = choice.lower()
        
    return choice

def decode_num(d):
    decode = ""
    
    if(d == 0):
        decode = "No"
    elif(d == 1):
        decode = "Yes"
    elif(d == 2):
        decode = "Needs Update"
    else:
        decode = "Error"
        
    return decode

def get_pos():
    pos = -1
    # Get position in row
    while(pos < 0 or pos > 2):
        space()
        try:
            pos = int(input("What position is this tote in the row: "))
        except ValueError:
            print("Enter a value")
            pos = -1
        
        
    return pos

def disp_need_bags_checks(t, n, o, l): # Display all OSNs with locations of needed bag checks
    print("\tOrders Not Assigned Bags\n\n")
    for i in range(len(t)):
        print("Order: \t" + o[i] + "\t" + n[i] + "\t" + t[i] + "\t" + l[i])
        
def get_lgst_num(nums): # Get the largest num
    largest = max(nums)
    
    return largest