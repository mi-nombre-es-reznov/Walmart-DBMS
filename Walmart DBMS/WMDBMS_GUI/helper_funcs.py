import csv

# import only system from os
from os import system, name
from collections import Counter

# define our clear function
def clear():

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def continues():
    '''
    c -- String: User input
    '''
    c = ""
    
    while(c != "y"):
        c = input("Continue? [y]: ")
        
        # Convert to lower
        c = c.lower()
        
def time_conv_hr(mil):
    civ = 0
    append = ":00:00"
    final_time = ""

    civ = (mil / 100) # Time less than 24

    if(civ == 12):
        final_time = "12:00:00"
    else:
        civ = int(civ)
        final_time = (str(civ) + append)
        
    return final_time

def get_unique_list(og):
    unique = []
    
    # Get the unique In Database values
    for i in range(len(og)):
        if(og[i] not in unique):
            unique.append(str(og[i]))
            
    return unique

def get_unique_list_tup(og):
    unique = []
    osn_remaining = []
    temp_tup = ()
    uni_osn = []
    ret_uni = []
    
    # Get the unique In Database values
    for i in range(len(og)):
        temp_tup = (og[i][0], og[i][1])
#        print(temp_tup)
        if(temp_tup not in unique):
            unique.append(temp_tup)
            
    for i in range(len(unique)):
        osn_remaining.append(unique[i][0])
        
#    print(osn_remaining)
    c = Counter(osn_remaining)
#    print(c)
    
    for i in range(len(c)):
        temp = c.popitem()
#        print(temp)

        if(temp[1] > 1):
            uni_osn.append(temp[0])
            
#    print(uni_osn)
    
    for i in range(len(uni_osn)):
        for j in range(len(unique)):
            if(uni_osn[i] == unique[j][0]):
                ret_uni.append(unique[j])
    
            
    return ret_uni

def get_alt_locs(h):
    alts = []
    
    for i in range(len(h)):
        temp = input("Scan for alt to " + h[i] + ": ")
        
        alts.append(temp)
        
    return alts

def test_csv(file_name):
    h = ['BR01', 'BR02', 'BR03', 'BR11', 'BR12', 'BR13', 'BR21', 'BR22', 'BR23', 'BR31', 'BR32', 'BR33']
    locs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

    # Test connection
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            
            for i in reader:                
                alt = i
    except FileNotFoundError:
        with open(file_name, 'w', newline = '') as f:
            
            writes = csv.writer(f)
            
            writes.writerow(h)
            writes.writerow(locs)

    return alt