def Menu_Banner():
    print("*************")
    print("* Main Menu *")
    print("*************\n\n")

def Menu(opt):
    '''
    - Input -
    opt -- List: Holds the names of the Menu items being passed in.
    choice -- Integer: Holds the representative value of the Menu item the user chose.
    
    - Output -
    ret: choice
    '''
    choice = 0
    
    # Create Menu banner
    Menu_Banner()
    
    # Iterate through the menu and display the number of items with choice marker
    for i in range(len(opt)):
        print(str(i + 1) + ") " + str(opt[i]))
        
    # Menu space
    print("\n\n")
        
    # Bound check for valid choice
    while(choice < 1 or choice > len(opt)):
        try:
            # Accept user input as an int and force repeat entry if invalid
            choice = int(input("Please select an option: "))
        except ValueError:
            choice = 0
            
    return choice

def input_data_Menu():
    print("***************")
    print("* Input Totes *")
    print("***************\n\n")
    
def staging_Menu():
    print("*****************")
    print("* Staging totes *")
    print("*****************\n\n")
    
def f_n_s_Menu():
    print("******************")
    print("* Find and Stage *")
    print("******************\n\n")
    
def curr_conf_Menu():
    print("*************************")
    print("* Current Configuration *")
    print("*************************\n\n")
    
def transfer_Menu():
    print("*****************")
    print("* Hour Transfer *")
    print("*****************\n\n")
    
def disp_tote_layout_Menu():
    print("BR01\tBR02\tBR03\t|\tBR11\tBR12\tBR13\t|\tBR21\tBR22\tBR23\t|\tBR31\tBR32\tBR33")
    print("----\t----\t----\t|\t----\t----\t----\t|\t----\t----\t----\t|\t----\t----\t----")