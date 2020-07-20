# v.1.1.1 - Nicholas Perez-Aguilar
import MySQLdb
import DBMSInsert as dbins
import DBMSRead as dbread
import misc_funcs as mf
import SQLqueries as sql
import Staging as stage
import stats as stat
import csv

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
                        loc = results[0][6]
                        bags = results[0][8]
                        
                        print("Location: " + str(loc))
                        print("OSN: " + str(osn))
                        
                        pass_for_exist.append(str(time_delta))
                        pass_for_exist.append(str(c_name))
                        pass_for_exist.append(str(osn))
                        pass_for_exist.append(str(ptype))
                        pass_for_exist.append(str(bags))
                            
                        # Pass useful data into exist write for
                        write_list = dbins.exist_write(pass_for_exist)
                        
                        # Reset list
                        pass_for_exist.clear()
                        
                        # Try and find existing locations
                        query2 = sql.get_spec_loc(str(loc), str(osn))
                        #print(query2)
                        
                        # Get location
                        try:
                            c.execute(query2)
                            resloc = c.fetchall()
                            
                            if(len(resloc) == 0):
                                print("No data returned from database")
                            else:
                                #print(str(resloc))
                                
                                loc2 = resloc[0][1]
                                pos2 = resloc[0][2]
                                
                                print("OSN " + str(osn) + " stored at row '" + loc2 + "', pos: " + str(pos2))
                        except:
                            db.rollback()
                            mf.space()
                            print("Error: Getting Current Location from Insertion")

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
                                
                                if(int(osn) > 100 and int(osn) < 999):
                                    # If exists, give location
                                    query = sql.get_poss_stage(table_stage, osn)
                                    
                                    # Try and get osn's location
                                    try:
                                        c.execute(query)
                                        ret = c.fetchall()
                                        
                                        #print("Ret res: " + str(ret))
                                        o = str(ret[0][0])
                                        l = str(ret[0][1])
                                        p = str(ret[0][2])
                                        
                                        if(len(ret) == 0):
                                            pass
                                        elif(str(p) == str(table_pos)):
                                            print(o + " staged at existing location!")
                                        else:
                                            print("Order " + o + " is stored in row " + l + " at position: " + p)
                                            
                                        print("\n\n")
                                    except:
                                        db.rollback()
                                        print("Error getting OSN from loc")
                            
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
                if(new_row == "UR01" or new_row == "UR11" or new_row == "TTF0" or new_row == "DS00"):
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
                            
                        if(new_row == "UR01" or new_row == "UR11" or new_row == "TTF0" or new_row == "DS00"):
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
            Stats_Items = ["General Tote Information", "Timed Deliveries", "Order Count", "Cancelled Orders", "Display Backroom Data", "Find Order"]
            count = 0
            q_choice = 0
                        
            choice = mf.Menu(Stats_Items)
            
            if(choice == 1):
                query = stat.get_groupings()
            elif(choice == 2):
                query = stat.get_deliveries_hour()
            elif(choice == 3):
                query = stat.get_order_cnt()
            elif(choice == 4):
                query = stat.cancelled_orders()
            elif(choice == 5):
                q_choice, query = stat.get_BR()
            elif(choice == 6):
                query = stat.find_order()
            else:
                print("Something went wrong!")
                mf.space()
            
            # Display Results
            try:
                c.execute(query)
                results = c.fetchall()
                
                if(len(results) == 0):
                    mf.space()
                    print("No data returned from DBMS")
                else:                    
                    # Switch through to find correct data from ret results
                    if(choice == 1):
                        cnt_list = []
                        a_list = []
                        c_list = []
                        f_list = []
                        u_list = []
                        n_list = []
                        a_cnt = 0
                        c_cnt = 0
                        f_cnt = 0
                        u_cnt = 0
                        n_cnt = 0
                        count = 0
                
                        try:
                            c.execute(query)
                            results = c.fetchall()
                            
                            # Get the OSN from each and push to specific type
                            for i in range(len(results)):
                                osn = str(results[i][4])
                                ttype = str(results[i][1])
                                
                                # Compare types for location pushing
                                if(ttype == "AMBIENT"):
                                    if(osn not in a_list):
                                        a_list.append(osn)
                                elif(ttype == "CHILLED"):
                                    if(osn not in c_list):
                                        c_list.append(osn)
                                elif(ttype == "FROZEN"):
                                    if(osn not in f_list):
                                        f_list.append(osn)
                                elif(ttype == "UNKNOWN"):
                                    if(osn not in u_list):
                                        u_list.append(osn)
                                elif(ttype == "None"):
                                    if(osn not in n_list):
                                        n_list.append(osn)
                                    
                                # Keep a global counter
                                count += 1
                                    
                            # Get the number of entries per list
                            a_cnt = len(a_list)
                            c_cnt = len(c_list)
                            f_cnt = len(f_list)
                            u_cnt = len(u_list)
                            n_cnt = len(n_list)
                            
                            # Push all length values into a list
                            cnt_list.append(a_cnt)
                            cnt_list.append(c_cnt)
                            cnt_list.append(f_cnt)
                            cnt_list.append(u_cnt)
                            cnt_list.append(n_cnt)
                                                
                            # Get max values
                            largest = mf.get_lgst_num(cnt_list)
                            stat.print_gen_res(largest, count, a_cnt, c_cnt, f_cnt, u_cnt, n_cnt, a_list, c_list, f_list, u_list, n_list)
                            
                        except:
                            db.rollback()
                            mf.space()
                            print("Error: General Data Fetching")
                        
                        # Reset values
                        cnt_list.clear()
                        a_list.clear()
                        c_list.clear()
                        f_list.clear()
                        u_list.clear()
                        n_list.clear()
                        a_cnt = 0
                        c_cnt = 0
                        f_cnt = 0
                        u_cnt = 0
                        n_cnt = 0
                    elif(choice == 2):
                        o_list = []
                        l_list = []
                        osn = ""
                        loc = ""
                        isin = False
                        
                        #print("Res: " + str(results))
                        
                        if(len(results) == 0):
                            print("No database results returned")
                        else:
                            for i in range(len(results)):
                                osn = str(results[i][0])
                                loc = str(results[i][1])
                                
                                if(osn not in o_list):
                                    o_list.append(osn)
                                    l_list.append(loc)
                                elif(osn in o_list): # Bound check for multiple locations
                                    for j in range(len(o_list)):
                                        if(o_list[j] == osn and l_list[j] == loc):
                                            isin = False
                                        elif(o_list[j] != osn):
                                            pass
                                        else:
                                            isin = True
                                            
                                        if(isin == True):
                                            o_list.append(osn)
                                            l_list.append(loc)
                                            break
                                        
                                    # Reset boolean
                                    isin = False
                            
                            # Display results            
                            for i in range(len(o_list)):
                                print(o_list[i] + "\t" + l_list[i])
                                
                            # Reset vals
                            o_list.clear()
                            l_list.clear()
                            osn = ""
                            loc = ""
                    elif(choice == 3):                        
                        # Get time
                        time = str(results[0][2])
                        
                        # Display description
                        print("Showing orders for requested time: " + time + '\n')
                        print("OSN\tLocation\tRow\tPosition\n---\t--------\t---\t--------")
                        
                        # Display results
                        #print("Res: " + str(results))
                        for i in range(len(results)):
                            osn = str(results[i][4])
                            loc = str(results[i][6])                            
                            count += 1
                            
                            # Get exact location with current loc and osn
                            if(loc == "unstaged"):
                                print(str(osn) + "\t" + str(loc) + "\tNULL\tNULL")
                            else:
                                query = sql.get_spec_loc(loc, osn)
                                loc = loc.replace('_', ' ')
                                #print("query: " + query)
                            
                                # Get location
                                try:
                                    c.execute(query)
                                    res = c.fetchall()
                                    #print("inner res: " + str(results))
                                    row = str(res[0][1])
                                    #print("Row top: " + row)
                                    

                                    if(row == 'UR01' or row == 'UR11'):
                                        pass
                                    else:
                                        #print("Res: " + str(results))
                                        pos = str(res[0][2])
                                            
                                    if(row == "UR01" or row == "UR11"):
                                        print(str(osn) + "\t" + str(loc) + "\t" + str(row) + "\tNone")
                                    else:
                                        print(str(osn) + "\t" + str(loc) + "\t" + str(row) + "\t" + str(pos))

                                except:
                                    db.rollback()
                                    mf.space()
                                    print("An error has occured with gathering the object location.")
                            

                        print("\n\nShowing a total of " + str(count) + " orders.")
                    elif(choice == 4):
                        # Display all cancelled osn's
                        for i in range(len(results)):
                            osn = results[i][4]
                            print(osn)
                            count += 1
                            
                        # Print final count
                        print("\n\nShowing a total of " + str(count) + " cancelled orders.")
                    elif(choice == 5):
                        osn_list = []
                        row_list = []
                        pos_list = []
                        b01 = []
                        b02 = []
                        b03 = []
                        b11 = []
                        b12 = []
                        b13 = []
                        b21 = []
                        b22 = []
                        b23 = []
                        b31 = []
                        b32 = []
                        b33 = []
                        dead = [] # Here for later
                        osn = ""
                        row = ""
                        pos = ""
                        li_o_li_format = []
                        count = 0
                        cnt_list = []
                        
                        #print("Res: " + str(results))
                        
                        if(len(results) == 0):
                            print("No data returned from DBMS")
                        else:
                            for i in range(len(results)):
                                # Get needed data
                                osn = str(results[i][0])
                                row = str(results[i][1])
                                pos = str(results[i][2])
                                
                                # Push to list
                                if(osn not in osn_list):
                                    osn_list.append(osn)
                                    row_list.append(row)
                                    pos_list.append(pos)
                                    
#                            print("osn: " + str(osn_list))
#                            print("row: " + str(row_list))
#                            print("pos: " + str(pos_list))
                                    
                            #print("Data unique complete")
                            # Push unique data to proper loc
                            li_o_li_format = mf.get_proper_staging_BR(osn_list, row_list, pos_list)
                            
                            #print("Test: " + str(li_o_li_format))
                            
                            # Assign to proper lists
                            b01 = li_o_li_format[0]
                            b02 = li_o_li_format[1]
                            b03 = li_o_li_format[2]
                            b11 = li_o_li_format[3]
                            b12 = li_o_li_format[4]
                            b13 = li_o_li_format[5]
                            b21 = li_o_li_format[6]
                            b22 = li_o_li_format[7]
                            b23 = li_o_li_format[8]
                            b31 = li_o_li_format[9]
                            b32 = li_o_li_format[10]
                            b33 = li_o_li_format[11]
                            
                            
                            # Keep a global counter
                            count += 1
                                    
                            # Get the number of entries per list
                            b01_cnt = len(b01)
                            b02_cnt = len(b02)
                            b03_cnt = len(b03)
                            b11_cnt = len(b11)
                            b12_cnt = len(b12)
                            b13_cnt = len(b13)
                            b21_cnt = len(b21)
                            b22_cnt = len(b22)
                            b23_cnt = len(b23)
                            b31_cnt = len(b31)
                            b32_cnt = len(b32)
                            b33_cnt = len(b33)
                            
                            # Push all length values into a list
                            cnt_list.append(b01_cnt)
                            cnt_list.append(b02_cnt)
                            cnt_list.append(b03_cnt)
                            cnt_list.append(b11_cnt)
                            cnt_list.append(b12_cnt)
                            cnt_list.append(b13_cnt)
                            cnt_list.append(b21_cnt)
                            cnt_list.append(b22_cnt)
                            cnt_list.append(b23_cnt)
                            cnt_list.append(b31_cnt)                            
                            cnt_list.append(b32_cnt)
                            cnt_list.append(b33_cnt)
                                                
                            # Get max values
                            largest = mf.get_lgst_num(cnt_list)
                            #print("largest: " + str(largest))
                            stat.print_BR_res(q_choice, largest, count, b01_cnt, b02_cnt, b03_cnt, b11_cnt, b12_cnt, b13_cnt, b21_cnt, b22_cnt, b23_cnt, b31_cnt, b32_cnt, b33_cnt, b01, b02, b03, b11, b12, b13, b21, b22, b23, b31, b32, b33)
                                                        
                    elif(choice == 6):
                        n_bags = 0
                        time = ""
                        bags = ""
                        loc = ""
                        osn = 0
                        tote = []
                        loc = []
                        e_loc = []
                        e_pos = []
                       
                        #print("Res: " + str(results))
                        
                        if(len(results) == 0):
                            print("No data returned from DBMS")
                        else:
                            # Get Time and bags
                            osn = str(results[0][0])
                            n_bag = str(results[0][4])
                            time = str(results[0][1])
                            
                            # Get all tote types and locs
                            for i in range(len(results)):
                                tote.append(results[i][2])
                                loc.append(results[i][3])
                                
                            # Get exact locs
                            for i in range(len(tote)):
                                if(loc[i] != "unstaged" or loc[i] != "Dead_Stage"):
                                    query = sql.get_spec_loc(loc[i], osn)
                                    #print(query)
                                    
                                    try:
                                        c.execute(query)
                                        res = c.fetchall()
                                    
                                        if(len(res) == 0):
                                            print("No data from DBMS")
                                        else:
#                                            print("a: " + str(res))
#                                            print("b: " + str(loc[i]))
                                            if(loc[i] == "Top_Shelf"):
                                                e_loc.append(row)
                                                e_pos.append("NULL")
                                            else:
                                                row = str(res[0][1])
                                                pos = str(res[0][2])
                                                
                                                
#                                                print("Row: " + row)
#                                                print("Pos: " + pos)
                                                e_loc.append(row)
                                                e_pos.append(pos)
#                                        print("eloc: " + str(e_loc))
#                                        print("epos: " + str(e_pos))
                                        
                                    except:
                                        mf.space()
                                        db.rollback()
                                        print("Error: Order location gathering")
                                else:
                                    e_loc.append("NULL")
                                    e_pos.append("NULL")
                                    
                            for k in range(len(tote)):
                                print(str(tote[k]) + "\t" + str(loc[k]) + "\t" + str(e_loc[k]) + "\t" + str(e_pos[k]))
                    else:
                        print("An error occurred!")
            except:
                db.rollback()
                mf.space()
                print("Error: Statistics Display")
        elif(usr_choice == 8):
            moveon = ""
            verify = ""
            mf.space()
            queries = []
            print("WARNING: THIS CANNOT BE UNDONE!!!!\n\n\n")
            
            while(moveon != 'y' and moveon != 'n'):
                # Ask to continue before moving on
                moveon = mf.get_y_n_choice("Continue? [Y/n] ")
                
            if(moveon == 'y'):
                while(verify != "WMDBMS"):
                    verify = input("Enter 'WMDBMS' to delete the database: ")
                    
                save_file = input("Enter a file name to save the main data before deletion! ")
                
                # Append extension to name
                save_file = (save_file + ".csv")
                
                query = sql.get_type_groupings()
                
                try:
                    c.execute(query)
                    results = c.fetchall()
                    title = ["Order Number", "Tote Type", "Due Time", "Customer Name", "OSN", "Pickup Type", "Location", "Dispensed", "Bags"]
                    #print(results)
                    
                    if(len(results) == 0):
                        print("Nothing to delete! Rolling back database")
                    else:
                        with open(save_file, 'w', newline = '') as file:
                            writer = csv.writer(file)
                            writer.writerow(title)
                            writer.writerows(results)
                            
                        print("Database write successful!")
                        
                        queries = sql.del_db()
                        
                        for i in range(len(queries)):
                            try:
                                c.execute(str(queries[i]))
                                db.commit()
                            except:
                                db.rollback()
                                print("Error: Delete table Data")
                                
                        print("All data has been deleted from the DBMS")
                except:
                    db.rollback()
                    mf.space()
                    print("Error: Database Deletion Data")
            elif(moveon == 'n'):
                mf.space()
                print("Database deletion has been exited with no changes!\n\n")
                main()
            else:
                print("Something Went Wrong at the Deletion Stage")
        else:
            print("Invalid choice")
            usr_choice = 0
         
        print("\n\n\n")
        query = "" # Reset as a precaution
        
        cont = ""
        while(cont != 'y'):
            # Ask to continue before moving on
            cont = mf.get_y_n_choice("Continue? [Y/n] ")
            
            if(cont == 'y'):
                pass
            
        # Reset for next output
        cont = 'n'
            
    
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