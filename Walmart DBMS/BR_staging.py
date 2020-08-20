# BR Staging - v1.0.0
# Nicholas Perez-Aguilar

import MySQLdb
import DBMSInsert as dbins
import DBMSRead as dbread
import misc_funcs as mf
import SQLqueries as sql
import Staging as stage
import stats as stat
import csv
# import only system from os
from os import system, name

global c
global db

# define our clear function
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

class ins_tote():
    def __init__(self, on, osn):
        self.order = on
        self.OSN = osn
        self.dispensed = 0
        self.time = ""
        
    def set_time(self, tme):
        self.time = tme
        
    def get_data(self):
        print("Order Num: " + str(self.order))
        print("OSN: " + str(self.OSN))
        print("Transfered: " + str(self.dispensed))
        print("Time: " + str(self.time))
        
        return self.order, self.OSN, self.dispensed, self.time

def get_order():
    order = ""
    
    while(order == ""):
        order = input("Scan tote: ")
        
    return order

def get_osn():
    osn = 0
    
    while(osn > 999 or osn < 100):
        try:
            osn = int(input("Enter OSN [100 -> 999]: "))
        except ValueError:
            osn = 0
            
    return osn
    
def main():
    order = ""
    osn = 0
    time = ""
   
    while 1:
        Menu() # Display Menu

def Menu():
    items = ["Insert New Tote", "Stage Tote", "Retrieve Tote Locations", "Transfer totes by hour", "Count OSN by hour", "Find Order", "Check for duplicates"]
    usr_choice = 0
    time_num = 0
    
    # Display Menu
    usr_choice = mf.Menu(items)
    clear()
    
    # Get choice
    if(usr_choice == 1):
        # Get tote data
        order = get_order()
        osn = get_osn()
        clear()
        
        # Create new entry
        tote = ins_tote(order, osn)
        
        # Test OSN for time check
        query = sql.test_osn_BR(osn)
        
        try:
            c.execute(query)
            res = c.fetchall()
            
            if(len(res) == 0):
                time_num = int(input("Insert due time (24-hr format): "))
                
                time = mf.time_conv_hr(time_num)
                #str("Time: " + str(time))
                
                tote.set_time(time)            
            else:
                print("OSN already exists") # For testing purposes
        except:
            mf.clear()
            db.rollback()
            print("Error: Testing OSN")
            
        order, osn, disp, time = tote.get_data()
        
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
                    print("Time write successful")
                except:
                    mf.clear()
                    print("Error: Writing time to DBMS")
                    db.rollback()
                    
            print("Tote write successful")
        except:
            mf.clear()
            print("Error: Writing tote to DBMS")
            db.rollback()

    elif(usr_choice == 2):
        tote = ""
        loc = ""
        query = ""
        
        tote = input("Scan tote: ")
        
        query = sql.find_order_BR(tote)
        
        try:
            c.execute(query)
            res = c.fetchall()
            
            if(len(res) == 0):
                print("No data found")
            else:
                osn = res[0][1]
                print("Data found!\nOSN: " + str(osn))
                
                query = sql.find_order_loc_BR(osn)
                
                try:
                    c.execute(query)
                    results = c.fetchall()
                    print("res: " + str(results))
                    
                    for i in range(len(results)):
                        if(results[i][0] != "Unstaged"):
                            mf.clear()
                            print(str(osn) + " staged at: " + str(results[i][0]))
                            break
                except:
                    mf.clear()
                    db.rollback()
                    print("Error: Getting staged location")
                    
                # Update staging
                loc = input("Scan location: ")
                query = sql.upd_staging_BR(tote, loc)
                
                try:
                    c.execute(query)
                    db.commit()
                    print(str(tote) + " staging updated!")
                except:
                    mf.clear()
                    db.rollback()
                    print("Error: Updating Staging Location")
        except:
            mf.clear()
            db.rollback()
            print("Error: Getting OSN from order")
    elif(usr_choice == 3):
        scans = []
        osns = []
        inter_osn = []
        res_un = []
        res_s = []
        res_nid = []
        BR01 = []
        BR02 = []
        BR03 = []
        BR11 = []
        BR12 = []
        BR13 = []
        BR21 = []
        BR22 = []
        BR23 = []
        BR31 = []
        BR32 = []
        BR33 = []
        str_locs = ["BR01", "BR02", "BR03", "BR11", "BR12", "BR13", "BR21", "BR22", "BR23", "BR31", "BR32", "BR33"]
        invalid = []
        valid = []
        max_num = []
        query = ""
        tote = ""
        tup = ()
        lgst = 0
        
        # Loop through and collect tote info
        while(tote != "END"):
            tote = input("Scan tote: ")
            
            if(tote != "END"):
                scans.append(tote)
            
        #print(scans)
        clear()
        
        # Get query and query results - OSN
        for i in range(len(scans)):
            query = sql.find_order_BR(str(scans[i]))
        
            try:
                c.execute(query)
                res = c.fetchall()

                # Get OSNs and place accordingly
                if(len(res) == 0):
                    res_nid.append(str(scans[i]))
                else:
                    print("Res: " + str(res))
                    for j in range(len(res)):
                        tup = (str(res[j][1]), str(res[j][2]))
                        inter_osn.append(tup)
                    

            except:
                #mf.clear()
                db.rollback()
                print("Error: Querying Database")


#        print(res_nid)
#        print(inter_osn)        
        
        if(len(res_nid) > 0):
            print("The following orders are not in the database:", end = " ")
            for i in range(len(res_nid)):
                print(res_nid[i], end = ", ")
            print("\n")
        
        # Set up data for displaying
        for i in range(len(inter_osn)):
            if(inter_osn[i][1] != "Unstaged"):
                if(inter_osn[i][1] == "BR01"):
                    if(str(inter_osn[i][0]) not in BR01):
                        BR01.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR02"):
                    if(str(inter_osn[i][0]) not in BR02):
                        BR02.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR03"):
                    if(str(inter_osn[i][0]) not in BR03):
                        BR03.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR11"):
                    if(str(inter_osn[i][0]) not in BR11):
                        BR11.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR12"):
                    if(str(inter_osn[i][0]) not in BR12):
                        BR12.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR13"):
                    if(str(inter_osn[i][0]) not in BR13):
                        BR13.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR21"):
                    if(str(inter_osn[i][0]) not in BR21):
                        BR21.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR22"):
                    if(str(inter_osn[i][0]) not in BR22):
                        BR22.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR23"):
                    if(str(inter_osn[i][0]) not in BR23):
                        BR23.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR31"):
                    if(str(inter_osn[i][0]) not in BR31):
                        BR31.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR32"):
                    if(str(inter_osn[i][0]) not in BR32):
                        BR32.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] == "BR33"):
                    if(str(inter_osn[i][0]) not in BR33):
                        BR33.append(str(inter_osn[i][0]))
                if(inter_osn[i][1] not in str_locs):
                    invalid.append((inter_osn[i][0], inter_osn[i][1]))
                    
#        print(BR01)
#        print(BR02)
#        print(BR03)
#        print(BR11)
#        print(BR12)
#        print(BR13)
#        print(BR21)
#        print(BR22)
#        print(BR23)
#        print(BR31)
#        print(BR32)
#        print(BR33)

        # Get all counts of data in lists
        br01c = len(BR01)
        br02c = len(BR02)
        br03c = len(BR03)
        br11c = len(BR11)
        br12c = len(BR12)
        br13c = len(BR13)
        br21c = len(BR21)
        br22c = len(BR22)
        br23c = len(BR23)
        br31c = len(BR31)
        br32c = len(BR32)
        br33c = len(BR33)
        
        # Place all lengths in array and find largest
        max_num.append(br01c)
        max_num.append(br02c)
        max_num.append(br03c)
        max_num.append(br11c)
        max_num.append(br12c)
        max_num.append(br13c)
        max_num.append(br21c)
        max_num.append(br22c)
        max_num.append(br23c)
        max_num.append(br31c)
        max_num.append(br32c)
        max_num.append(br33c)
        
        lgst = mf.get_lgst_num(max_num)
        #print("Lgst: " + str(lgst))
        
        
        # Send data to be displayed
        stat.Print_Backroom_Staging(lgst, br01c, br02c, br03c, br11c, br12c, br13c, br21c, br22c, br23c, br31c, br32c, br33c, BR01, BR02, BR03, BR11, BR12, BR13, BR21, BR22, BR23, BR31, BR32, BR33)
        
        # Display invalid data
        if(len(invalid) > 0):
            print("\n\nInvalid Location Order Numbers:", end = " ")
            
            for i in range(len(invalid)):
                print(invalid[i], end = " ")
        
            print("\n")
            
        # Ask user to auto stage
        
        # Auto stage
        
        # Reset data
        scans.clear()
        osns.clear()
        inter_osn.clear()
        res_un.clear()
        res_s.clear()
        res_nid.clear()
        query = ""
        tote = ""
        
    elif(usr_choice == 4):
        hour = 0
        time = ""
        osns = []
        
        hour = int(input("Transfering hour: "))
        time = mf.time_conv_hr(hour)
        
        query = sql.upd_transfer_get_osn_BR(time)
        
        # Get osn, update transfered...
        try:
            c.execute(query)
            res = c.fetchall()
            
            # Get OSN by hour
            for i in range(len(res)):
                osns.append(res[i])
            
            # Update each OSN
            for i in range(len(osns)):
                query = sql.upd_transfer_status(str(osns[i][0]))
                
                try:
                    c.execute(query)
                    db.commit()
                except:
                    mf.clear()
                    db.rollback()
                    print("Error: Updating OSN by hour")
                    
            print("All values updated!")
        except:
            mf.clear()
            db.rollback()
            print("Error: Getting OSN")
    elif(usr_choice == 5):
        query = ""
        time_int = 0
        time = ""
        
        # Get hour from user
        while(time_int > 2000 or time_int < 700):
            try:
                time_int = int(input("Enter hour to count: "))
            except:
                print("Enter a valid hour")
                
        # Get query with chosen hour
        time = mf.time_conv_hr(time_int)
        query = sql.get_cnt_hr_BR(time)
        
        try:
            c.execute(query)
            res = c.fetchall()
            
            mf.clear()
            print("There are a total of " + str(res[0][0]) + " orders for: " + time)
        except:
            mf.clear()
            db.rollback()
            print("Error: Getting order count")
    elif(usr_choice == 6):
        unique = []
        query, osn = stat.find_order_BR()
        
        try:
            c.execute(query)
            res = c.fetchall()
            if(len(res) == 0):
                print("No data returned from DBMS")
            else:
                #print(str(res))
                for i in range(len(res)):
                    if(str(res[i][0]) not in unique):
                        unique.append(str(res[i][0]))

                for i in range(len(unique)):
                    print("Location for order " + str(osn) + ": " + unique[i])
        except:
            mf.clear()
            db.rollback()
            print("Error: Getting order location")
    elif(usr_choice == 7):
        pass
    else:
        print("Something went wrong")
    
    # Clear screen
    choice = 'n'
    while(choice == 'n'):
        choice = mf.get_y_n_choice("\nContinue [Y/n]: ")

    clear()
        
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
        mf.clear()
        print("Thanks for using NCompEng Technologies!\n\nSee you soon!!!\n")
        pass