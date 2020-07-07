# v.1.1.1 - Nicholas Perez-Aguilar
import MySQLdb
import DBMSInsert as dbins
import DBMSRead as dbread
import misc_funcs as mf
import SQLqueries as sql
import Staging as stage

global c
global db

def main():
    usr_choice = 0
    Menu_items = ["Insert Into Database", "Read From Database", "Stage", "Change Staging Locations", "Dispense", "Bag Check", "Clear Database"]
    ins_choices = ["Insert New Object", "Insert with Existing OSN"]
    write_list = []
    query = ""
    q_vals = ""
    exist_OSN = ""
    results = []
    pass_for_exist = []
    message = "OSN does not exist in database. Create new object? [Y/n] "
    on = ""
    stage_loc = ""
    table_stage = ""
    table_row = ""
    pos = -1
    tote = ""
    
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
            mf.space()
            while(on != "-1"):
                on = input("Enter tote to stage [-1 to exit]: ")
                
                # If user doesn't want to exit
                if(on != "-1"):
                    query = sql.get_OSN(on)
                    
                    # Test if OSN can be reached
                    try:
                        c.execute(query)
                        result = c.fetchall()
                        
                        if(len(result) == 0):
                            print("Object does not exist!!!")
                        else:
                            osn = str(result[0][0])

                            # Get table and row for query
                            while(table_stage == "Invalid" or table_row == "Null" or table_stage == "" or table_row == ""):
                                stage_loc = input("Scan (or Enter) the staging location: ")
                                table_stage, table_row = stage.decode_loc(stage_loc)
                                mf.space()    
                        
                            # Get position
                            pos = mf.get_pos()
                            table_pos = str(pos)
                            
#                            print("OSN: " + osn)
#                            print("Table Loc: " + table_stage)
#                            print("Table Row: " + table_row)
#                            print("Table Pos: " + table_pos)
                            
                            # Get query for updating Object data
                            upd_main = sql.update_stage_loc(table_stage, osn, on)
                            
                            # Update main file with staged table
                            try:
                                c.execute(upd_main)
                                db.commit()
                                mf.space()
                                print("OSN '" + osn + "' location has been successfully updated!")
                            except:
                                db.rollback()
                                mf.space()
                                print("Error: Updating object location")
                                
                            # Get query for inserting row and pos into chosen table
                            update_loc_insert = sql.insert_stage_loc_pos(table_stage, osn, table_row, table_pos)
                            #print("Query: " + update_loc_insert)
                            try:
                                c.execute(update_loc_insert)
                                db.commit()
                                mf.space()
                                print("Success: Table Stage has been updated")
                            except:
                                db.rollback()
                                mf.space()
                                print("Error: Updating location table with write")
                            
                            # Reset Values
                            osn = ""
                            table_stage = ""
                            table_row = ""
                    except:
                        print("Error: GET OBJECT OSN STAGE")
                else:
                    mf.space()
                    print("Staging has been exited!")
        elif(usr_choice == 4):
            while(tote == "" or tote != "-1" or new_loc == "" or new_loc != "-1"):
                tote = input("Scan a tote [or order number] to change staging area [-1 to exit]: ")
                
                # Test break
                if(tote == "-1"):
                    tote = ""
                    break
                
                new_loc_ins = input("Scan a new staging area [-1 to exit]: ")
                
                # Test break
                if(new_loc_ins == "-1"):
                    new_loc_ins = ""
                    break
                
                new_loc, new_row = stage.decode_loc(new_loc_ins)
                pos = mf.get_pos()
                str_pos = str(pos)

                # Pull all data about unison of totes
                query = sql.read_tote(tote)
                
                try:
                    # Read tote data
                    c.execute(query)
                    write_list = c.fetchall()
                    
                    if(len(write_list) == 0):
                        mf.space()
                        print("Query returned 0 results")
                    else:
                        mf.space()
                        #print("writelist: " + str(write_list))
                        
                        on = write_list[0][0] # Order Num
                        osn = write_list[0][4] # OSN
                        loc = write_list[0][6] # Location from main
                        
                        # Find curr location and delete old entry
                        query = sql.del_old_loc(loc, osn)
                        
                        try:
                            c.execute(query)
                            db.commit()
                            mf.space()
                            print("Old Table: Deletion Succesful")
                        except:
                            db.rollback()
                            mf.space()
                            print("Error: Old Table Deletion Failure")
                            
                        # Update location in main
                        query = sql.update_stage_loc_bulk(osn, loc, new_loc)
                        
                        try:
                            c.execute(query)
                            db.commit()
                            mf.space()
                            print("Bulk Staging update: Successful")
                        except:
                            db.rollback()
                            mf.space()
                            print("Error: Bulk Update Failure")
                            
                        # Write new location in table
                        query = sql.insert_stage_loc_pos(new_loc, osn, new_row, pos)
                        
                        # Reset values for next entry
                        new_loc = ""
                        osn = ""
                        new_row = ""
                        pos = ""
                        
                        # Execute write query
                        try:
                            c.execute(query)
                            db.commit()
                            mf.space()
                            print("Table Write Successful")
                        except:
                            db.rollback()
                            mf.space()
                            print("Error: Table Write Failure")
                except:
                    mf.space()
                    print("Error: Tote Read Failure")
                    db.rollback()
                    
                    
        elif(usr_choice == 5):
            print("Dispensing coming soon!")
        elif(usr_choice == 6):
            print("Bag Check coming soon!")
        elif(usr_chioce == 7):
            print("Database Clearing coming soon!")
        else:
            print("Invalid choice")
            usr_choice = 0
         
        print("\n\n\n")
        query = "" # Reset as a precaution
    
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