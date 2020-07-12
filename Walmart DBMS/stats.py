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