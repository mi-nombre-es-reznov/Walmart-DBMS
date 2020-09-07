global c
global db

import MySQLdb
import Menu_options as MO
import helper_funcs as hf
import Insert as ins
import SQL_queries as sql
import Staging as stage
import curr_conf as cconf
    
def main():
    '''
    - Input -
    MM -- List: Main Menu, Menu Options
    M_choice -- Integer: Holds the user choice
    query -- String: Holds a query in SQL format
    
    - Output -
    Null
    '''
    MM = ["Input totes", "Staging", "Find and Stage", "Current configuration", "Transfer totes by hour"]
    M_choice = 0
    order = ""
    temp = ""
    Location = ""
    Totes = []
    osn = 0
    disp = 0
    time = 0
    
    while True:
        M_choice = MO.Menu(MM) # Display Menu
        
        # Insert into database
        if(M_choice == 1):
            hf.clear()
            MO.input_data_Menu()
            query, order, osn = ins.tote_data_gathering()
            
            try:
                c.execute(query)
                res = c.fetchall()
                
                if(len(res) == 0):
                    order, osn, disp, time = ins.time_tote_ins(order, osn)
                else:
                    order, osn, disp, time = ins.get_class_data(order, osn)
                    print("OSN already exists") # For testing purposes
            except:
                mf.clear()
                db.rollback()
                print("Error: Testing OSN")
                
            #order, osn, disp, time = ins.get_class_data()
            
            #print("Order: " + str(order) + "\nosn: " + str(osn) + "\ndisp: " + str(disp) + "\ntime: " + str(time))
            
            # Push data to Database
            query = sql.ins_tote_BR(order, osn, disp)
            
            try:
                c.execute(query)
                db.commit()
                
                if(time != ""):
                    query = sql.ins_time_BR(osn, time)
                    
                    try:
                        c.execute(query)
                        db.commit()
                        
                        # Switch to LEDs later
                        print("Time write successful")
                    except:
                        hf.clear()
                        db.rollback()
                        
                        # Include LEDs later
                        print("Error: Writing time to DBMS")
                        
                # --- Change later to LED ---
                print("Tote write successful")
            except:
                hf.clear()
                db.rollback()
                
                # Include LEDs later
                print("Error: Writing tote to DBMS")
        # Stage in database
        elif(M_choice == 2):
            invalid = []
            
            hf.clear()
            MO.staging_Menu()
            Location, Totes = stage.get_staging_info()
            
            # Pass each tote through for query-location pairing
            for i in range(len(Totes)):
                query = stage.get_query_stage(Location, Totes[i])
                
                try:
                    c.execute(query)
                    db.commit()
                    
                    # Update later with LED
                    print("Staging successful")
                except:
                    hf.clear()
                    db.rollback()
                    print("Error: Update staging location")
                    invalid.append(Totes[i])
                    
                if(len(invalid) > 0):
                    print("Invalid totes...\n")
                    
                    for i in range(len(invalid)):
                        print(invalid[i])
        # Find and Stage
        elif(M_choice == 3):
            hf.clear()
            MO.f_n_s_Menu()
        # Show current config of BR
        elif(M_choice == 4):
            query = ""
            li_of_li = []
            
            hf.clear()
            MO.curr_conf_Menu()

            query = cconf.get_staged_items()
            try:
                c.execute(query)
                res = c.fetchall()                
                li_of_li = cconf.seperate_staged_data(res)                    
                cconf.disp_tote_layout(li_of_li)
            except:
                db.rollback()
                hf.clear()
                print("Error: Getting Staged items")
        # Update DBMS to transfer totes by hour
        elif(M_choice == 5):
            print("Transfer totes by hour")
            
        # Ask to continue
        hf.continues()
        hf.clear()
        
        # Reset values
        M_choice = 0
        
# Establish a connection and bound check phpmyadmin and python boundaries
if(__name__ == '__main__'):
    try:
        db = MySQLdb.connect("localhost","root","WMDBMS","Walmart Backroom Staging")
        c = db.cursor()
        
        print("\nConnection Established!\n\n")
    except:
        print("Server Connection Failed!")
        
    try:
        main()
    except KeyboardInterrupt:
        hf.clear()
        print("Thanks for using NCompEng Technologies!\n\nSee you soon!!!\n")
        pass