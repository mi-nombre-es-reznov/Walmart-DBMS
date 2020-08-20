# v.1.1.1 - Nicholas Perez-Aguilar
import misc_funcs as mf
import SQLqueries as sql

def get_order_cnt(): # Get the number of orders for a given hour
    new_time = 0
    time = ""
    
    # Get the requested hour
    while(new_time > 2000 or new_time < 700):
        try:
            new_time = int(input("Pick an hour [0700 -> 2000]: "))
        except ValueError:
            print("Enter a valid number!\n")

    time = mf.time_conv_hr(new_time)
    
    # Get the query after passing in hour
    query = sql.hour_order_cnt(time)
    
    # Return search query
    return query

def cancelled_orders(): # Display cancelled message and return query
    mf.space()
    print("Cancelled Orders\n\nOSN\n---")
    query = sql.get_cancelled()
    
    return query

def get_groupings(): # Get the groupings ('Ambient, 'Frozen, etc.) and OSN's
    mf.space()
    print("\t\t\t\tGeneral Statistics\n")
    print("AMBIENT\t\tCHILLED\t\tFROZEN\t\tUNKNOWN\t\tNone")
    print("------\t\t-------\t\t------\t\t-------\t\t----")
    
    query = sql.get_type_groupings()
    
    return query

def print_gen_res(lgst, cnt, ac, cc, fc, uc, nc, al, cl, fl, ul, nl): # This will take all the lists and print the results
    atmp = ""
    ctmp = ""
    ftmp = ""
    utmp = ""
    ntmp = ""
    
    # Check each list to make sure that the length is not being exceeded
    for i in range(lgst):
        # Ambient
        if(i > (ac - 1)):
            atmp = ""
        else:
            atmp = al[i]
            
        # Chilled
        if(i > (cc - 1)):
            ctmp = ""
        else:
            ctmp = cl[i]
            
        # Frozen
        if(i > (fc - 1)):
            ftmp = ""
        else:
            ftmp = fl[i]
            
        # Unknown
        if(i > (uc - 1)):
            utmp = ""
        else:
            utmp = ul[i]
            
        # None
        if(i > (nc - 1)):
            ntmp = ""
        else:
            ntmp = nl[i]
            
#        print("Current i: " + str(i))
#        print("Largest: " + str(lgst))
#        print("Count: " + str(cnt))
            
        print(str(atmp) + "\t\t" + str(ctmp) + "\t\t" + str(ftmp) + "\t\t" + str(utmp) + "\t\t" + str(ntmp))

def get_deliveries_hour(): # Get query for deliveries in specified hour
    time = 0
    t_str = ""
    
    try:
        while(time < 700 or time > 2000):
            time = int(input("Enter hour to search: "))

        t_str = mf.time_conv_hr(time)
    except ValueError:
        print("Enter a valid number")
    
    mf.space()
    print("Deliveries for: {0}\n\nOSN\tLocation\n---\t--------".format(t_str))
    query = sql.get_deliveries_time(t_str)
    
    return query

def find_order(): # Query to find an order and it's locations
    osn = 0 
    try:
        while(osn > 999 or osn < 100):
            osn = int(input("Enter OSN: "))
    except ValueError:
        print("Enter a valid number")
            
    query = sql.get_order_osn(osn)

    mf.space()
    print("Finding Order for: {0}\n\n Type \tLocation\tRow\tPosition\n------\t--------\t---\t--------".format(osn))
    
    return query

def get_BR(): # Get the backroom data
    choice = ""
    choices = ["First", "Second", "Dead"]
    
    mf.space()
    
    print("BR01\tBR02\tBR03\t|\tBR11\tBR12\tBR13\t|\tBR21\tBR22\tBR23\t|\tBR31\tBR32\tBR33")
    print("----\t----\t----\t|\t----\t----\t----\t|\t----\t----\t----\t|\t----\t----\t----")
#    choice = mf.Menu(choices)    
#    if(choice == 1):
#        # Display description
#        print("Showing Current Back Room Orders: OSN | Pos\n")
#        print("BR01\tBR02\tBR03\tBR11\tBR12\tBR13")
#        print("----\t----\t----\t----\t----\t----")
#    elif(choice == 2):
#        # Display description
#        print("Showing Current Back Room Orders: OSN | Pos\n")
#        print("BR21\tBR22\tBR23\tBR31\tBR32\tBR33")
#        print("----\t----\t----\t----\t----\t----")
#    elif(choice == 3):
#        print("Dead Stage Data coming soon!")
#    else:
#        print("Something went wrong!")
    
    query = sql.get_BR_curr()
    
    return choice, query
    #print("|492 | 0|\n|-------|\n|469 | 0|")

def print_BR_res(lgst, b01c, b02c, b03c, b11c, b12c, b13c, b21c, b22c, b23c, b31c, b32c, b33c, b01, b02, b03, b11, b12, b13, b21, b22, b23, b31, b32, b33): # This will take all the lists and print the results
    b01tmp = ""
    b02tmp = ""
    b03tmp = ""
    b11tmp = ""
    b12tmp = ""
    b13tmp = ""
    b21tmp = ""
    b22tmp = ""
    b23tmp = ""
    b31tmp = ""
    b32tmp = ""
    b33tmp = ""
    tup = ()
    
    #print("Choice: " + str(choice))

    # Check each list to make sure that the length is not being exceeded
    for i in range(lgst):
        if(i > (b01c - 1)):
            b01tmp = ""
        else:
            tup = b01[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b01tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b02c - 1)):
            b02tmp = ""
        else:
            tup = b02[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b02tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b03c - 1)):
            b03tmp = ""
        else:
            tup = b03[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b03tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b11c - 1)):
            b11tmp = ""
        else:
            tup = b11[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b11tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b12c - 1)):
            b12tmp = ""
        else:
            tup = b12[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b12tmp = (tmp1 + " | " + tmp2)
  
        if(i > (b13c - 1)):
            b13tmp = ""
        else:
            tup = b13[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b13tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b21c - 1)):
            b21tmp = ""
        else:
            tup = b21[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b21tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b22c - 1)):
            b22tmp = ""
        else:
            tup = b22[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b22tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b23c - 1)):
            b23tmp = ""
        else:
            tup = b23[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b23tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b31c - 1)):
            b31tmp = ""
        else:
            tup = b31[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b31tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b32c - 1)):
            b32tmp = ""
        else:
            tup = b32[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b32tmp = (tmp1 + " | " + tmp2)
            
        if(i > (b33c - 1)):
            b33tmp = ""
        else:
            tup = b33[i]
            tmp1 = tup[0]
            tmp2 = tup[1]
            b33tmp = (tmp1 + " | " + tmp2)
            
#        print("Current i: " + str(i))
#        print("Largest: " + str(lgst))
#        print("Count: " + str(cnt))

        print(str(b01tmp) + "\t" + str(b02tmp) + "\t" + str(b03tmp) + "\t\t" + str(b11tmp) + "\t" + str(b12tmp) + "\t" + str(b13tmp) + "\t\t" + str(b21tmp) + "\t" + str(b22tmp) + "\t" + str(b23tmp) + "\t\t" + str(b31tmp) + "\t" + str(b32tmp) + "\t" + str(b33tmp))

#        if(choice == 1):
#            print(str(b01tmp) + "\t" + str(b02tmp) + "\t" + str(b03tmp) + "\t" + str(b11tmp) + "\t" + str(b12tmp) + "\t" + str(b13tmp))
#        elif(choice == 2):
#            print(str(b21tmp) + "\t" + str(b22tmp) + "\t" + str(b23tmp) + "\t" + str(b31tmp) + "\t" + str(b32tmp) + "\t" + str(b33tmp))
#        else:
#            print("Something went wrong!")

def find_order_BR(): # Query to find an order and it's locations
    osn = 0 
    try:
        while(osn > 999 or osn < 100):
            osn = int(input("Enter OSN: "))
    except ValueError:
        print("Enter a valid number")
            
    query = sql.get_order_osn_BR(osn)

    mf.space()
    #print("Finding Order for: {0}".format(osn))
    
    return query, osn

def Print_Backroom_Staging(lgst, b01c, b02c, b03c, b11c, b12c, b13c, b21c, b22c, b23c, b31c, b32c, b33c, b01, b02, b03, b11, b12, b13, b21, b22, b23, b31, b32, b33): # This will take all the lists and print the results
    b01tmp = ""
    b02tmp = ""
    b03tmp = ""
    b11tmp = ""
    b12tmp = ""
    b13tmp = ""
    b21tmp = ""
    b22tmp = ""
    b23tmp = ""
    b31tmp = ""
    b32tmp = ""
    b33tmp = ""

    print("\n")
    print("BR01\tBR02\tBR03\t|\tBR11\tBR12\tBR13\t|\tBR21\tBR22\tBR23\t|\tBR31\tBR32\tBR33")
    print("----\t----\t----\t|\t----\t----\t----\t|\t----\t----\t----\t|\t----\t----\t----")

    # Check each list to make sure that the length is not being exceeded
    for i in range(lgst):
        if(i > (b01c - 1)):
            b01tmp = ""
        else:
            b01tmp = b01[i]
            
        if(i > (b02c - 1)):
            b02tmp = ""
        else:
            b02tmp = b02[i]
            
        if(i > (b03c - 1)):
            b03tmp = ""
        else:
            b03tmp = b03[i]
            
        if(i > (b11c - 1)):
            b11tmp = ""
        else:
            b11tmp = b11[i]
            
        if(i > (b12c - 1)):
            b12tmp = ""
        else:
            b12tmp = b12[i]
  
        if(i > (b13c - 1)):
            b13tmp = ""
        else:
            b13tmp = b13[i]
            
        if(i > (b21c - 1)):
            b21tmp = ""
        else:
            b21tmp = b21[i]
            
        if(i > (b22c - 1)):
            b22tmp = ""
        else:
            b22tmp = b22[i]
            
        if(i > (b23c - 1)):
            b23tmp = ""
        else:
            b23tmp = b23[i]
            
        if(i > (b31c - 1)):
            b31tmp = ""
        else:
            b31tmp = b31[i]
            
        if(i > (b32c - 1)):
            b32tmp = ""
        else:
            b32tmp = b32[i]
            
        if(i > (b33c - 1)):
            b33tmp = ""
        else:
            b33tmp = b33[i]

        print(str(b01tmp) + "\t" + str(b02tmp) + "\t" + str(b03tmp) + "\t\t" + str(b11tmp) + "\t" + str(b12tmp) + "\t" + str(b13tmp) + "\t\t" + str(b21tmp) + "\t" + str(b22tmp) + "\t" + str(b23tmp) + "\t\t" + str(b31tmp) + "\t" + str(b32tmp) + "\t" + str(b33tmp))
