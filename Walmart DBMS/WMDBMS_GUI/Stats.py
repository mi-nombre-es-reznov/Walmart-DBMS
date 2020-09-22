def sep_hours(data):
    eight = []
    nine = []
    ten = []
    eleven = []
    twelve = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    
#    print(data)
    for i in range(len(data)):
        osn = str(data[i][0])
        time = str(data[i][2])
#        print(osn)
#        print(time)
        
        if(time == "8:00:00"):
            if(osn not in eight):
                eight.append(osn)

        if(time == "9:00:00"):
            if(osn not in nine):
                nine.append(osn)
                
        if(time == "10:00:00"):
            if(osn not in ten):
                ten.append(osn)
                
        if(time == "11:00:00"):
            if(osn not in eleven):
                eleven.append(osn)

        if(time == "12:00:00"):
            if(osn not in twelve):
                twelve.append(osn)
                
        if(time == "13:00:00"):
            if(osn not in one):
                one.append(osn)
                
        if(time == "14:00:00"):
            if(osn not in two):
                two.append(osn)

        if(time == "15:00:00"):
            if(osn not in three):
                three.append(osn)
                
        if(time == "16:00:00"):
            if(osn not in four):
                four.append(osn)
                
        if(time == "17:00:00"):
            if(osn not in five):
                five.append(osn)

        if(time == "18:00:00"):
            if(osn not in six):
                six.append(osn)
                
        if(time == "19:00:00"):
            if(osn not in seven):
                seven.append(osn)
                
#    print(eight)
#    print(nine)
#    print(ten)
#    print(eleven)
#    print(twelve)
#    print(one)
#    print(two)
#    print(three)
#    print(four)
#    print(five)
#    print(six)
#    print(seven)
    
    print("Currently staged hours and counts")
    print("---------------------------------\n")
    if(len(eight) > 0):
        print("0800: " + str(len(eight)))
        
    if(len(nine) > 0):
        print("0900: " + str(len(nine)))
        
    if(len(ten) > 0):
        print("1000: " + str(len(ten)))
        
    if(len(eleven) > 0):
        print("1100: " + str(len(eleven)))
    
    if(len(twelve) > 0):
        print("1200: " + str(len(twelve)))
        
    if(len(one) > 0):
        print("1300: " + str(len(one)))
        
    if(len(two) > 0):
        print("1400: " + str(len(two)))
        
    if(len(three) > 0):
        print("1500: " + str(len(three)))
        
    if(len(four) > 0):
        print("1600: " + str(len(four)))
        
    if(len(five) > 0):
        print("1700: " + str(len(five)))
        
    if(len(six) > 0):
        print("1800: " + str(len(six)))
        
    if(len(seven) > 0):
        print("1900: " + str(len(seven)))
        
    print("\n\n")