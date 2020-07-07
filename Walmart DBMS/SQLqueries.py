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

def del_old_loc(table, osn): # Deletes the location of the OSN from the non-main tables
    query = ("DELETE FROM {0} WHERE OSN = '{1}';".format(table, osn))
    
    return query

def update_stage_loc_bulk(osn, old_loc, new_loc): # Updates multiples totes in a location by OSN
    query = ("UPDATE Create_Objs SET Location = '{0}' WHERE OSN = '{1}' and Location = '{2}';".format(new_loc, osn, old_loc))
    
    return query