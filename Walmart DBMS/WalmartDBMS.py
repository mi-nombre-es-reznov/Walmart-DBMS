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
    Menu_items = ["Insert Into Database", "Read From Database", "Stage", "Change Staging Locations", "Dispense", "Bag Check", "Statistics", "Clear Database"]
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
                            
                            if(table_row == "UR01" or table_row == "UR11"):
                                pass
                            else:
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
                            if(table_row == "UR01" or table_row == "UR11"):
                                update_loc_insert = sql.insert_stage_top(table_stage, osn, table_row)
                            else:
                                update_loc_insert = sql.insert_stage_loc_pos(table_stage, osn, table_row, table_pos)
                            #print("Query: " + update_loc_insert)
                            
                            try:
                                c.execute(update_loc_insert)
                                db.commit()
                                print("Success: Table Stage has been updated")
                            except:
                                db.rollback()
                                mf.space()
                                print("Error: Updating location table with write")
                            
                            # Reset Values
                            osn = ""
                            table_stage = ""
                            table_row = ""
                            table_pos = ""
                            update_loc_insert = ""
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
                if(new_row == "UR01" or new_row == "UR11"):
                    pass
                else:
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
                            
                        if(new_row == "UR01" or new_row == "UR11"):
                            query = sql.insert_stage_top(new_loc, osn, new_row)
                        else:
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
            Dispensing_Menu = ["Dispense", "Return", "Cancel"]
            usr_choice = ""
            OSN = ""
                    
            while(tote == ""):
                usr_choice = mf.Menu(Dispensing_Menu)
                tote = input("Scan a tote [or enter Order Number]: ")
                
                if(tote == "-1"):
                    break
                
            # Get OSN from order num
            query = sql.get_OSN(tote)
            
            try:
                c.execute(query)
                results = c.fetchall()
                
                OSN = str(results[0][0])
                mf.space()
                print("OSN obtained!")
            except:
                db.rollback()
                mf.space()
                print("OSN failed to be obtained!")
                main()
                
            if(usr_choice == 1):
                update = 1
            elif(usr_choice == 2):
                update = 0
            elif(usr_choice == 3):
                update = 2
            else:
                mf.space()
                print("Something went wrong!")
                main()
            
            # Update dispense field
            query = sql.disp_ret_canc_update(update, OSN)
            
            try:
                c.execute(query)
                db.commit()
                mf.space()
                print("Dispensing updated!")
            except:
                db.rollback()
                mf.space()
                print("Error: Dispensing Update Failure")
                
            # Reset values
            tote = ""            
        elif(usr_choice == 6):
            bags = ""
            check = ""
            choice = ""
            bag_choice = ["View All Unspecified Orders", "Update Order"]
            times = []
            names = []
            OSNs = []
            Locs = []
            new_times = []
            new_names = []
            new_osns = []
            new_locs = []
            onum = ""
            
            check = mf.Menu(bag_choice)
            
            if(check == 1):
                query = sql.check_for_bags()
                
                try:
                    c.execute(query)
                    results = c.fetchall()
                    mf.space()
                    #print("Results: " + str(results))
                    
                    for i in range(len(results)):
                        times.append(str(results[i][0]))
                        names.append(str(results[i][1]))
                        OSNs.append(str(results[i][2]))
                        Locs.append(str(results[i][3]))
                    
                    for i in range(len(results)):
                        if(OSNs[i] not in new_times and names[i] != "None"):
                            new_times.append(times[i])
                            new_names.append(names[i])
                            new_osns.append(OSNs[i])
                            new_locs.append(Locs[i])
                    
                    mf.disp_need_bags_checks(new_times, new_names, new_osns, new_locs)
                except:
                    db.rollback()
                    mf.space()
                    print("Error: Bag Check Failure")
            elif(check == 2):
                while(onum == ""):
                    onum = input("Scan tote [or enter Order Number]: ")
                    query = sql.get_OSN(onum)
                    
                    try:
                        c.execute(query)
                        results = c.fetchall()
                        mf.space()
                        
                        if(len(results) == 0):
                            print("No data returned from DBMS")
                        else:
                            upd = mf.get_y_n_choice("Does this order require bags [Y/n]: ")
                            print("Update: " + upd)
                            
                            if(upd == 'n'):
                                check = "0"
                            elif(upd == 'y'):
                                check = "1"
                            else:
                                print("Error: Bag Check")
                            
                            OSN = str(results[0][0])
                            query = sql.update_bags(check, OSN)
                            
                            try:
                                c.execute(query)
                                db.commit()
                                mf.space()
                                print("Bag Check Update Successful!")
                            except:
                                db.rollback()
                                mf.space()
                                print("Error: Bag Check Update")
                    except:
                        db.rollback()
                        mf.space()
                        print("Error: Tote Data Failure")
                        
                # Reset Values
                bags = ""
                check = ""
                choice = ""
                times.clear()
                names.clear()
                OSNs.clear()
                Locs.clear()
                new_times.clear()
                new_names.clear()
                new_osns.clear()
                new_locs.clear()
                onum = ""
                        
            else:
                print("Something went wrong!")
                
        elif(usr_choice == 7):
            print("Statistics page coming soon!")
        elif(usr_choice == 8):
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