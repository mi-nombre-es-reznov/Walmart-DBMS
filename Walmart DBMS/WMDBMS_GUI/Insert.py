import helper_funcs as hf
import SQL_queries as sql

class ins_tote():
    def __init__(self, on, osn):
        self.order = on
        self.OSN = osn
        self.dispensed = 0
        self.time = ""
        
    def set_time(self, tme):
        self.time = tme
        
    def get_data(self):
        print("Order Num: " + str(self.order))
        print("OSN: " + str(self.OSN))
        print("Transfered: " + str(self.dispensed))
        print("Time: " + str(self.time))
        
        return self.order, self.OSN, self.dispensed, self.time
    
def get_order():
    order = ""
    
    while(order == ""):
        order = input("Scan tote: ")
        
    return order

def get_osn():
    osn = 0
    
    while(osn > 999 or osn < 100):
        try:
            osn = int(input("Enter OSN [100 -> 999]: "))
        except ValueError:
            osn = 0
            
    return osn

def tote_data_gathering():
    '''
    --- Input ---
    pass
    
    --- Output ---
    order -- String: Holds the Order Number of a tote (i.e. K#####)
    osn -- Integer: Holds the OSN of the Order.
    query -- String: Holds the current query to be passed to the database
    tote -- class object: Holds the object of the data to the ins_tote class.
    '''
    # Get tote data
    order = get_order()
    osn = get_osn()
    hf.clear()
    
    # Create new entry
    tote = ins_tote(order, osn)
    
    # Test OSN for time check
    query = sql.test_osn_BR(osn)
    
    return query, order, osn

def time_tote_ins(order, osn):
    time_num = 0
    
    time_num = int(input("Insert due time (24-hr format): "))
    
    time = hf.time_conv_hr(time_num)
    #str("Time: " + str(time))
    
    tote = ins_tote(order, osn)
    tote.set_time(time)
    
    order, osn, disp, time = tote.get_data()

    return order, osn, disp, time
    
def get_class_data(order, osn):
    tote = ins_tote(order, osn)

    order, osn, disp, time = tote.get_data()
    