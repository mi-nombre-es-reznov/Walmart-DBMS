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
    query = ("SELECT * FROM Create_Objs WHERE OSN = '{0}'".format(osn))
    
    return query