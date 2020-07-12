# v.1.1.1 - Nicholas Perez-Aguilar
def insert_new_obj(listdata): # Inserts data into the DBMS for a new object
    query = ""
    data = ""
    
    data = ("VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}');".format(str(listdata[0]), str(listdata[1]), str(listdata[2]), str(listdata[3]), str(listdata[4]), str(listdata[5]), str(listdata[6]), str(listdata[7]), str(listdata[8])))
    query = ("INSERT INTO Create_Objs (Order_Num, Type, Due_Time, Cust_Name, OSN, Pickup_Type, Location, Dispensed, Bags)" + data)
    
    return query

def read_all_db_data(): # Returns exactly what DBMS gives
    query = ("SELECT * FROM Create_Objs;")
    
    return query

def test_OSN(osn):
    query = ("SELECT * FROM Create_Objs WHERE OSN = '{0}';".format(osn))
    
    return query

def read_tote(k): # Reads all data tied to tote object (Order Num)
    query = ("SELECT * FROM Create_Objs WHERE Order_Num = '{0}';".format(k))
    
    return query

def read_order(k): # Reads all totes that have the requested OSN number
    query = ("SELECT * FROM Create_Objs WHERE OSN = '{0}';".format(k))
    
    return query

def get_OSN(k): # Uses the order number to get the OSN
    query = ("SELECT OSN FROM Create_Objs WHERE Order_Num = '{0}';".format(k))
    
    return query

def update_stage_loc(loc, osn, order_num): # Update main data OSN location
    query = ("UPDATE Create_Objs SET Location = '{0}' WHERE OSN = '{1}' and Order_Num = '{2}';".format(loc, osn, order_num))
    
    return query

def insert_stage_loc_pos(table, osn, row, pos): # Insert the stage location and position in tied table
    query = ("INSERT INTO {0}(OSN, Row, Pos) VALUES('{1}', '{2}', '{3}');".format(table, osn, row, pos))
    
    return query

def insert_stage_top(table, osn, side): # Insert top and side
    query = ("INSERT INTO {0}(OSN, Side) VALUES('{1}', '{2}');".format(table, osn, side))
    
    return query

def del_old_loc(table, osn): # Deletes the location of the OSN from the non-main tables
    query = ("DELETE FROM {0} WHERE OSN = '{1}';".format(table, osn))
    
    return query

def update_stage_loc_bulk(osn, old_loc, new_loc): # Updates multiples totes in a location by OSN
    query = ("UPDATE Create_Objs SET Location = '{0}' WHERE OSN = '{1}' and Location = '{2}';".format(new_loc, osn, old_loc))
    
    return query

def disp_ret_canc_update(upd, osn): # This query either dispenses, returns, or cancels orders
    query = ("UPDATE Create_Objs SET Dispensed = '{0}' WHERE OSN = {1};".format(upd, osn))
    
    return query

def check_for_bags(): # This query checks the database for all orders that have no bag decision
    query = ("SELECT Due_Time, Cust_Name, OSN, Location FROM `Create_Objs` WHERE Dispensed = 0 and Bags = 2")
    
    return query

def update_bags(upd, osn): # Update bag check
    query = ("UPDATE Create_Objs SET Bags = '{0}' WHERE OSN = '{1}';".format(upd, osn))
    
    return query

def hour_order_cnt(t): # Query that grabs all orders within requested hour
    query = ("SELECT * FROM `Create_Objs` WHERE Due_Time = '{0}' GROUP BY OSN;".format(t))
    
    return query

def get_spec_loc(loc, osn): # Query to grab the specific order's location
    query = ("SELECT * FROM {0} WHERE OSN = '{1}';".format(loc, osn))
    
    return query

def get_cancelled(): # Get all cancelled orders
    query = ("SELECT * FROM `Create_Objs` WHERE Dispensed = '2';")
    
    return query

def get_type_groupings(): # Get all groupings with no dups in OSN
    query = ("SELECT * FROM `Create_Objs`;")
    
    return query

def get_deliveries_time(hour): # Pull all deliveries for a specified hour
    query = ("SELECT OSN, Location FROM `Create_Objs` WHERE Pickup_Type = 'Delivery' and Due_Time = '{0}'".format(hour))
    
    return query

def get_order_osn(osn): # Get an order from the database via an OSN number
    query = ("SELECT OSN, Due_Time, Type, Location, Bags FROM `Create_Objs` WHERE OSN = '{0}'".format(osn))
    
    return query