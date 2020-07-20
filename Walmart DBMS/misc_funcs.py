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

def get_proper_staging_BR(o_li, r_li, p_li): # Gets the proper staging from the database for the Back Room
    b01 = []
    b02 = []
    b03 = []
    b11 = []
    b12 = []
    b13 = []
    b21 = []
    b22 = []
    b23 = []
    b31 = []
    b32 = []
    b33 = []
    ret_li = []
    
    ret_li.clear()
    
#    print(o_li)
#    print(r_li)
#    print(p_li)
    
    for i in range(len(r_li)):
        if(r_li[i] == "BR01"):
            b01.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR02"):
            b02.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR03"):
            b03.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR11"):
            b11.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR12"):
            b12.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR13"):
            b13.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR21"):
            b21.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR22"):
            b22.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR23"):
            b23.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR31"):
            b31.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR32"):
            b32.append((str(o_li[i]), str(p_li[i])))
        elif(r_li[i] == "BR33"):
            b33.append((str(o_li[i]), str(p_li[i])))
        else:
            print("An error occurred with OSN: " + o_li[i])
            
    # Push into giant list
    ret_li.append(b01)
    ret_li.append(b02)
    ret_li.append(b03)
    ret_li.append(b11)
    ret_li.append(b12)
    ret_li.append(b13)
    ret_li.append(b21)
    ret_li.append(b22)
    ret_li.append(b23)
    ret_li.append(b31)
    ret_li.append(b32)
    ret_li.append(b33)

    #print("Inner append: " + str(ret_li))
    return ret_li