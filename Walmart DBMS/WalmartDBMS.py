# v.1.1.1 - Nicholas Perez-Aguilar
'''

'''
import MySQLdb
import DBMSInsert as ins
import misc_funcs as mf

global c
global db

def main():
    usr_choice = 0
    Menu_items = ["Insert Into Database", "Read From Database", "Stage", "Dispense", "Bag Check"]
    write_list = []
    query = ""
    q_vals = ""
    
    while True:
        usr_choice = mf.Menu(Menu_items)
        
        # Case Statements equivalent -- not really...
        if(usr_choice == 1):
            write_list = ins.write()
            
            # Test returned values
            #print(write_list)

            q_vals = ("VALUES ('" + str(write_list[0]) + "', '" + str(write_list[1]) + "', '" + str(write_list[2]) + "', '" + str(write_list[3]) + "', '" + str(write_list[4]) + "', '" + str(write_list[5]) + "', '" + str(write_list[6]) + "', '" + str(write_list[7]) + "', '" + str(write_list[8]) + "');")
            query = ("INSERT INTO Create_Objs (Order_Num, Type, Due_Time, Cust_Name, OSN, Pickup_Type, Location, Dispensed, Bags) " + q_vals)
            
            try:
                #print(query)
                c.execute(query)
                db.commit()
                mf.space()
                print("Write succesful!")
            except:
                db.rollback()
                mf.space()
                print("An error has occurred!")
                
        elif(usr_choice == 2):
            ins.read()
        elif(usr_choice == 3):
            print("Staging coming soon!")
        elif(usr_choice == 4):
            print("Dispensing coming soon!")
        elif(usr_choice == 5):
            print("Bag Check coming soon!")
        else:
            print("Invalid choice")
         
        print("\n\n\n")
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
