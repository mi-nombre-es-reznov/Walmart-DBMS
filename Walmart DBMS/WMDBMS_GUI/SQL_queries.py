def test_osn_BR(osn):
    query = ("SELECT * FROM `Main` WHERE OSN = '{0}'".format(osn))
    
    return query

def ins_tote_BR(order, osn, di):
    query = ("INSERT INTO `Main`(Order_Num, OSN, Location, Transfered) VALUES('{0}', '{1}', 'Unstaged', '{2}');".format(order, osn, di))
    
    return query

def ins_time_BR(osn, time):
    query = ("INSERT INTO Times(OSN, Time) VALUES('{0}', '{1}');".format(osn, time))
    
    return query

def stage_curr_tote(l, c):
    query = ("UPDATE `Main` SET `Location` = '{0}' WHERE `Order_Num` = '{1}';".format(l, c))
    
    return query

def staged_list():
    query = ("SELECT `OSN`, `Location` FROM `Main` WHERE Location != 'Unstaged' and Transfered = 0;")

    return query

def get_osns_from_time(t):
    query = ("SELECT `OSN` FROM `Times` WHERE `Time` = '{0}';".format(t))
    
    return query

def update_main_osn_time(osn):
    query = ("UPDATE `Main` SET `Transfered` = 1 WHERE `OSN` = '{0}';".format(osn))
    
    return query

def check_tote_DB(tote):
    query = ("SELECT `OSN` FROM `Main` WHERE `Order_Num` = '{0}';".format(tote))
    
    return query

def tote_loc(osn):
    query = ("SELECT `Location` FROM `Main` WHERE `OSN` = '{0}' and `Location` != 'Unstaged';".format(osn))
    
    return query

def find_dups():
    query = ("SELECT `OSN` FROM `Times`;")
    
    return query

def get_query_totes(osn):
    query = ("SELECT `Location` FROM `Main` WHERE `OSN` = '{0}' and `Transfered` = '0' and `Location` != 'Unstaged';".format(osn))
    
    return query

def find_osn_loc(osn):
    query = ("SELECT `OSN`, `Location` FROM `Main` WHERE `OSN` = '{0}';".format(osn))
    
    return query

def drop_view_test():
    query = ("DROP VIEW IF EXISTS `FULL_DB`;")
    
    return query
    
def view_main_times():
    query = ("CREATE VIEW `FULL_DB` AS SELECT m.OSN, m.Location, t.Time FROM `Main` AS m INNER JOIN `Times` AS t ON m.OSN = t.OSN WHERE `Location` != 'Unstaged' and `Transfered` = 0;")
    
    return query

def staged_list_times():
    query = ("SELECT `OSN`, `Location` FROM `Main` WHERE Location != 'Unstaged' and Transfered = 0;")

    return query

def view_data():
    query = ("SELECT * FROM `FULL_DB`;")
    
    return query