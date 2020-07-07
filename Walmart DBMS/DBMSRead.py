import misc_funcs as mf
import SQLqueries as sql

def read():
    options = ["All Data", "Read Tote Data", "Read Order"]
    usr_choice = 0
    order_num = ""
    
    mf.space()
    usr_choice = mf.Menu(options)
    
    if(usr_choice == 1):
        mf.space()
        query = sql.read_all_db_data()
        
    elif(usr_choice == 2):
        mf.space()
        
        order_num = input("Please enter the Order Num: ")
        query = sql.read_tote(order_num)
    elif(usr_choice == 3):
        mf.space()
        
        order_num = input("Please scan a tote with your requested OSN: ")
        query = sql.get_OSN(order_num)
    else:
        print("Invalid choice: Please select a valid option!")
        
    return query