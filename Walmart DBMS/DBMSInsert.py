# v.1.1.1 - Nicholas Perez-Aguilar
import misc_funcs as mf

class create_tote():
    def __init__(self, order_num, due_time, OSN):
        self.on = order_num
        self.tt = None
        self.dt = due_time
        self.cn = None
        self.osn = OSN
        self.pt = None
        self.loc = "unstaged"
        self.disp = 0
        self.bags = 2
        
    def set_vals(self, tote_type, cust_name, P_type, bags): # Add bags
        self.tt = tote_type
        self.cn = cust_name
        self.pt = P_type
        self.bags = bags
        
    def get_vals(self):
        print("Order Number: " + str(self.on))
        print("Tote Type: " + str(self.tt))
        print("Due Time: " + str(self.dt))
        print("Customer Name: " + str(self.cn))
        print("OSN: " + str(self.osn))
        print("Pickup Type: " + str(self.pt))
        print("Location: " + str(self.loc))
        print("Dispensed? " + str(self.disp))
        print("Bags? " + str(self.bags))
        print("\n\n\n")
        
        return ([self.on, self.tt, self.dt, self.cn, self.osn, self.pt, self.loc, self.disp, self.bags])
        
def get_on():
    order_num = ""
    
    # Get base data for obj creation
    while(order_num == ""):
        order_num = input("Requesting Order Number: ") # Order Number: KXXXXX - unique

    return order_num

def get_time():
    time = 0
    due_time = ""
    while(time > 2000 or time < 700):
        time = int(input("Requesting due time - hr only [0700 -> 2000]: "))
    
    due_time = mf.time_conv_hr(time) # Convert to 12-hr format
    
    return due_time

def get_osn():
    OSN = 0
    
    while(OSN < 100 or OSN > 1000):
        try:
            OSN = int(input("Requesting OSN [100 -> 1000]: ")) # Valid OSN - not unique
        except ValueError:
            print("\nEnter a number!\n")
            OSN = 0

    return OSN

def get_totetype():
    totes = ["AMBIENT", "CHILLED", "FROZEN", "UNKNOWN"]
    tote_choice = 0
    tote_type = ""
    tote_choice = mf.Menu(totes)
    
    # Get tote type
    if(tote_choice == 1):
        tote_type = totes[0]
    elif(tote_choice == 2):
        tote_type = totes[1]
    elif(tote_choice == 3):
        tote_type = totes[2]
    elif(tote_choice == 4):
        tote_type = totes[3]
    else:
        print("An error has occurred!")

    return tote_type

def get_cust():
    cust_name = ""
    # Get Customer name
    while(len(cust_name) < 1 or len(cust_name) > 7):
        cust_name = input("Requesting customer name [AS ON LABEL]: ") # Cust name

    return cust_name

def get_pickup():
    p_types = ["CURBSIDE", "DELIVERY"]
    p_choice = 0

    # Get pickup
    p_choice = mf.Menu(p_types)
        
    # Get pickup type
    if(p_choice == 1):
        pickup = p_types[0]
    elif(p_choice == 2):
        pickup = p_types[1]
    else:
        print("An error has occurred!")

    return pickup

def get_bags(ptype):
    # --- Bag Check ---
    if(ptype == "DELIVERY"):
        bags = 1
    else:
        bags = 2

    return bags

def write():
    # Variables
    usr_choice = ""
    order_num = "" # To be scanned in
    time = 0
    due_time = ""
    OSN = 0
    tote_type = ""
    cust_name = ""
    pickup = ""
    ret_list = []
    bags = 0
    
    mf.space()
    
    # Pick the short or long entry
    while(usr_choice != "n" and usr_choice != "y"):
        usr_choice = input("Would you like to create a full object? [Y/n] ")
        
        usr_choice = usr_choice.lower()
        
    order_num = get_on()
    due_time = get_time()
    OSN = get_osn()
    
    # Create object for tote
    order = create_tote(order_num, due_time, OSN)

    if(usr_choice == 'y'):
        # Get rest of data
        tote_type = get_totetype()
        cust_name = get_cust()
        pickup = get_pickup()
        bags = get_bags(pickup)

    
        # View random data
        order.set_vals(tote_type, cust_name, pickup, bags)
    
    # Display results
    mf.space()
    ret_list = order.get_vals()
    
    # Delete pre-existing objects
    del order
    
    # Return the list
    return ret_list

def exist_write(existing):
    order_num = get_on() # Get OSN from user
    due_time = existing[0] # Get due time from existing data
    OSN = existing[2] # Get OSN from existing data
    tote_type = get_totetype() # Get tote type from user 
    cust_name = existing[1] # Get Customer name from existing data
    pickup = existing[3] # Get pickup type from existing data
    bags = existing[4] # Get bags from existing data
    
    # Create object with existing data
    order = create_tote(order_num, due_time, OSN)
    order.set_vals(tote_type, cust_name, pickup, bags)
    
    mf.space()
    # Display results
    ret_list = order.get_vals()
    
    del order
    
    return ret_list
