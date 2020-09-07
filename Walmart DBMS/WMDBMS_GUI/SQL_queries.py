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