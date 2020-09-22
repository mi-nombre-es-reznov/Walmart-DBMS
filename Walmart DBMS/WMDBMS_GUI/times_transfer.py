import helper_funcs as hf
import SQL_queries as sql

def get_transfer_time():
    time_num = 0
    
    time_num = int(input("Insert due time (24-hr format): "))
    time = hf.time_conv_hr(time_num)
    
    query = sql.get_osns_from_time(time)
    
    return query

def update_transfer_time(osn):
    query = sql.update_main_osn_time(osn)
    
    return query