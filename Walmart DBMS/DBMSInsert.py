# v.1.1.1 - Nicholas Perez-Aguilar
'''

'''
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
    totes = ["AMBIENT", "CHILLED", "FROZEN", "UNKNOWN"]
    tote_choice = 0
    p_types = ["CURBSIDE", "DELIVERY"]
    p_choice = 0
    ret_list = []
    bags = 0
    
    print("\n\nInput the data into the database...\n\n\n")
    
    # Pick the short or long entry
    while(usr_choice != "n" and usr_choice != "y"):
        usr_choice = input("Would you like to create a full object? ")
        
        usr_choice = usr_choice.lower()
        
    # Get base data for obj creation
    while(order_num == ""):
        order_num = input("Requesting Order Number: ") # Order Number: KXXXXX - unique
            
    while(time > 2000 or time < 700):
        time = int(input("Requesting due time - hr only [0700 -> 2000]: "))
    
    due_time = mf.time_conv_hr(time) # Convert to 12-hr format
    
    while(OSN < 100 or OSN > 1000):
        try:
            OSN = int(input("Requesting OSN [100 -> 1000]: ")) # Valid OSN - not unique
        except ValueError:
            print("\nEnter a number!\n")
            OSN = 0
    
    # Create object for tote
    order = create_tote(order_num, due_time, OSN)

    if(usr_choice == 'y'):
        # Get rest of data
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
    
        # Get Customer name
        while(len(cust_name) < 1 or len(cust_name) > 7):
            cust_name = input("Requesting customer name [AS ON LABEL]: ") # Cust name
        
        
        # Get pickup
        p_choice = mf.Menu(p_types)
            
        # Get pickup type
        if(p_choice == 1):
            pickup = p_types[0]
        elif(p_choice == 2):
            pickup = p_types[1]
        else:
            print("An error has occurred!")
            
        # --- Bag Check ---
        if(pickup == "DELIVERY"):
            bags = 1
        else:
            bags = 2

    
        # View random data
        order.set_vals(tote_type, cust_name, pickup, bags)
    
    # Display results
    mf.space()
    ret_list = order.get_vals()
    
    # Delete pre-existing objects
    del order
    
    # Return the list
    return ret_list
    
def read():
    print("Read coming soon")