# v.1.1.1 - Nicholas Perez-Aguilar
import MySQLdb
import DBMSInsert as dbins
import DBMSRead as dbread
import misc_funcs as mf
import SQLqueries as sql

global c
global db

def main():
    usr_choice = 0
    Menu_items = ["Insert Into Database", "Read From Database", "Stage", "Dispense", "Bag Check"]
    ins_choices = ["Insert New Object", "Insert with Existing OSN"]
    write_list = []
    query = ""
    q_vals = ""
    exist_OSN = ""
    results = []
    pass_for_exist = []
    message = "OSN does not exist in database. Create new object? [Y/n] "
    
    while True:
        usr_choice = mf.Menu(Menu_items)
        
        # Case Statements equivalent -- not really...
        if(usr_choice == 1):
            mf.space()
            
            usr_choice = mf.Menu(ins_choices)
            mf.space()
            
            if(usr_choice == 1):
                write_list = dbins.write()
            elif(usr_choice == 2):
                # Get OSN from user
                OSN = dbins.get_osn()
                
                # Test OSN against DBMS
                query = sql.test_OSN(OSN)
                
                try:
                    c.execute(query)
                    results = c.fetchall()
                    mf.space()
                                        
                    if(len(results) == 0):
                        choice = mf.get_y_n_choice(message)
                        
                        if(choice == 'y'):
                            write_list = dbins.write()
                        else:
                            main()
                    else:
                        time_delta = results[0][2]
                        c_name = results[0][3]
                        osn = results[0][4]
                        ptype = results[0][5]
                        bags = results[0][8]
                        
#                        print("Time delta: " + str(time_delta))
#                        print("Customer name: " + str(c_name))
#                        print("OSN: " + str(osn))
#                        print("Pickup Type: " + str(ptype))
                            
                        pass_for_exist.append(str(time_delta))
                        pass_for_exist.append(str(c_name))
                        pass_for_exist.append(str(osn))
                        pass_for_exist.append(str(ptype))
                        pass_for_exist.append(str(bags))
                            
                        # Pass useful data into exist write for
                        write_list = dbins.exist_write(pass_for_exist)
                        
                        # Reset list
                        pass_for_exist.clear()

                except:
                    print("Error: OSN Read Failure")
                    db.rollback()
                    mf.space()
            else:
                print("Error: Insertion choice")
            
            query = sql.insert_new_obj(write_list)
            
            try:
                c.execute(query)
                db.commit()
                mf.space()
                print("Write successful!")
            except:
                db.rollback()
                mf.space()
                print("An error has occurred at the database level!\nVerify the object has not already been inserted before retrying!")
                
        elif(usr_choice == 2):
            query = dbread.read()
            
            # Used to get the OSN from the Order Number
            if("SELECT OSN FROM" in query):
                try:
                    c.execute(query)
                    result = c.fetchall()
                    
                    if(len(result) == 0):
                        print("No results returned from database!")
                    else:
                        osn = result[0][0]
                        
                        # Get query using OSN to find objects
                        query = sql.read_order(osn)
                except:
                    print("Something went wrong!")
                
            mf.space()
            
            try:
                c.execute(query)
                result = c.fetchall()
                
                if(len(result) == 0):
                    print("No results returned from database!")
                else:
                    for i in range(len(result)):
                        on = result[i][0]
                        tt = result[i][1]
                        time = result[i][2]
                        name = result[i][3]
                        osn = result[i][4]
                        ptype = result[i][5]
                        loca = result[i][6]
                        disp = result[i][7]
                        need_bag = result[i][8]
                    
                        dispensed = mf.decode_num(disp)
                        bags = mf.decode_num(need_bag)
                        
                        print("\n\n")
                        print("Order Number: " + str(on))
                        print("Tote Type: " + str(tt))
                        print("Due Time: " + str(time))
                        print("Customer Name: " + str(name))
                        print("OSN: " + str(osn))
                        print("Pickup: " + str(ptype))
                        print("Location: " + str(loca))
                        print("Dispensed: " + str(dispensed))
                        print("Bags: " + str(bags))
            except:
                print("Something went wrong!")
        elif(usr_choice == 3):
            print("Staging coming soon!")
        elif(usr_choice == 4):
            print("Dispensing coming soon!")
        elif(usr_choice == 5):
            print("Bag Check coming soon!")
        else:
            print("Invalid choice")
            usr_choice = 0
         
        print("\n\n\n")
        query = "" # Reset as a precaution
        #mf.space()


    
# Establish a connection and bound check phpmyadmin and python boundaries
if(__name__ == '__main__'):
    try:
        db = MySQLdb.connect("localhost","root","WMDBMS","Walmart DBMS")
        c = db.cursor()
        
        print("\nConnection Established!\n\n")
    except:
        print("Server Connection Failed!")
        
    try:
        main()
    except KeyboardInterrupt:
        mf.space()
        print("Thanks for using NCompEng Technologies!\n\nSee you soon!!!\n")
        pass
