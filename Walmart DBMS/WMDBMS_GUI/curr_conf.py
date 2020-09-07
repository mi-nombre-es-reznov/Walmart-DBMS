import helper_funcs as hf
import SQL_queries as sql
import Menu_options as MO

def get_staged_items():
    query = ""
    
    query = sql.staged_list()
    
    return query

def seperate_staged_data(results):
    osns = ""
    locs = ""
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
    li_of_li = []
    
    # Iterate through results and place in appropriate lists
    for i in range(len(results)):
        osns = str(results[i][0])
        locs = str(results[i][1])
        
        if((locs == "BR01") and (osns not in BR01)):
            BR01.append(osns)
        elif((locs == "BR02") and (osns not in BR02)):
            BR02.append(osns)
        elif((locs == "BR03") and (osns not in BR03)):
            BR03.append(osns)
        elif((locs == "BR11") and (osns not in BR11)):
            BR11.append(osns)
        elif((locs == "BR12") and (osns not in BR12)):
            BR12.append(osns)
        elif((locs == "BR13") and (osns not in BR13)):
            BR13.append(osns)
        elif((locs == "BR21") and (osns not in BR21)):
            BR21.append(osns)
        elif((locs == "BR22") and (osns not in BR22)):
            BR22.append(osns)
        elif((locs == "BR23") and (osns not in BR23)):
            BR23.append(osns)
        elif((locs == "BR31") and (osns not in BR31)):
            BR31.append(osns)
        elif((locs == "BR32") and (osns not in BR32)):
            BR32.append(osns)
        elif((locs == "BR33") and (osns not in BR33)):
            BR33.append(osns)
            
    # Concate lists
    li_of_li.append(BR01)
    li_of_li.append(BR02)
    li_of_li.append(BR03)
    li_of_li.append(BR11)
    li_of_li.append(BR12)
    li_of_li.append(BR13)
    li_of_li.append(BR21)
    li_of_li.append(BR22)
    li_of_li.append(BR23)
    li_of_li.append(BR31)
    li_of_li.append(BR32)
    li_of_li.append(BR33)
    
    return li_of_li

def disp_tote_layout(lol):
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
    BR01c = 0
    BR02c = 0
    BR03c = 0
    BR11c = 0
    BR12c = 0
    BR13c = 0
    BR21c = 0
    BR22c = 0
    BR23c = 0
    BR31c = 0
    BR32c = 0
    BR33c = 0
    counts = [BR01c, BR02c, BR03c, BR11c, BR12c, BR13c, BR21c, BR22c, BR23c, BR31c, BR32c, BR33c]
    t1 = ""
    t2 = ""
    t3 = ""
    t4 = ""
    t5 = ""
    t6 = ""
    t7 = ""
    t8 = ""
    t9 = ""
    t10 = ""
    t11 = ""
    t12 = ""
    max_count = 0
    
    # Get counts of every list in lol
    for i in range(len(lol)):
        counts[i] = len(lol[i])
            
    # Get max count
    max_count = max(counts)
    
    # Display in order
    MO.disp_tote_layout_Menu()
    
    BR01 = lol[0]
    BR02 = lol[1]
    BR03 = lol[2]
    BR11 = lol[3]
    BR12 = lol[4]
    BR13 = lol[5]
    BR21 = lol[6]
    BR22 = lol[7]
    BR23 = lol[8]
    BR31 = lol[9]
    BR32 = lol[10]
    BR33 = lol[11]
    
    for i in range(max_count):
        if(i < counts[0]):
            t1 = BR01[i]
        else:
            t1 = ""
            
        if(i < counts[1]):
            t2 = BR02[i]
        else:
            t2 = ""
            
        if(i < counts[2]):
            t3 = BR03[i]
        else:
            t3 = ""
            
        if(i < counts[3]):
            t4 = BR11[i]
        else:
            t4 = ""
            
        if(i < counts[4]):
            t5 = BR12[i]
        else:
            t5 = ""
            
        if(i < counts[5]):
            t6 = BR13[i]
        else:
            t6 = ""
            
        if(i < counts[6]):
            t7 = BR21[i]
        else:
            t7 = ""
            
        if(i < counts[7]):
            t8 = BR22[i]
        else:
            t8 = ""
            
        if(i < counts[8]):
            t9 = BR23[i]
        else:
            t9 = ""
            
        if(i < counts[9]):
            t10 = BR31[i]
        else:
            t10 = ""
            
        if(i < counts[10]):
            t11 = BR32[i]
        else:
            t11 = ""
            
        if(i < counts[11]):
            t12 = BR33[i]
        else:
            t12 = ""
            
        print(t1 + "\t" + t2 + "\t" + t3 + "\t|\t" + t4 + "\t" + t5 + "\t" + t6 + "\t|\t" + t7 + "\t" + t8 + "\t" + t9 + "\t|\t" + t10 + "\t" + t11 + "\t" + t12)
        
    print("\n\n")