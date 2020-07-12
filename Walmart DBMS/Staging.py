# v.1.1.1 - Nicholas Perez-Aguilar

def decode_loc(l):
    decode = ""
    row = ""
    
    if(l == "SR01" or l == "1010011010100100011000000110001"):
        decode = "Staging"
        row = "SR01"
    elif(l == "SR02" or l == "1010011010100100011000000110010"):
        decode = "Staging"
        row = "SR02"
    elif(l == "SR03" or l == "1010011010100100011000000110011"):
        decode = "Staging"
        row = "SR03"
    elif(l == "SR04" or l == "1010011010100100011000000110100"):
        decode = "Staging"
        row = "SR04"
    elif(l == "TR01" or l == "1010100010100100011000000110001"):
        decode = "Transfer_Zero"
        row = "TR01"
    elif(l == "TR02" or l == "1010100010100100011000000110010"):
        decode = "Transfer_Zero"
        row = "TR02"
    elif(l == "TR03" or l == "1010100010100100011000000110011"):
        decode = "Transfer_Zero"
        row = "TR03"
    elif(l == "TR11" or l == "1010100010100100011000100110001"):
        decode = "Transfer_One"
        row = "TR11"
    elif(l == "TR12" or l == "1010100010100100011000100110010"):
        decode = "Transfer_One"
        row = "TR12"
    elif(l == "TR13" or l == "1010100010100100011000100110011"):
        decode = "Transfer_One"
        row = "TR13"
    elif(l == "DR01" or l == "1000100010100100011000000110001"):
        decode = "Dispensing"
        row = "DR01"
    elif(l == "DR02" or l == "1000100010100100011000000110001"):
        decode = "Dispensing"
        row = "DR02"
    elif(l == "DR03" or l == "1000100010100100011000000110011"):
        decode = "Dispensing"
        row = "DR03"
    elif(l == "LR01" or l == "1001100010100100011000000110001"):
        decode = "Late"
        row = "LR01"
    elif(l == "LR02" or l == "1001100010100100011000000110010"):
        decode = "Late"
        row = "LR02"
    elif(l == "UR01" or l == "1010101010100100011000000110001"):
        decode = "Top_Shelf"
        row = "UR01"
    elif(l == "UR11" or l == "1010101010100100011000100110001"):
        decode = "Top_Shelf"
        row = "UR11"
    elif(l == "BR01" or l == "1000010010100100011000000110001"):
        decode = "Back_Room"
        row = "BR01"
    elif(l == "BR02" or l == "1000010010100100011000000110010"):
        decode = "Back_Room"
        row = "BR02"
    elif(l == "BR03" or l == "1000010010100100011000000110011"):
        decode = "Back_Room"
        row = "BR03"
    elif(l == "BR11" or l == "1000010010100100011000100110001"):
        decode = "Back_Room"
        row = "BR11"
    elif(l == "BR12" or l == "1000010010100100011000100110010"):
        decode = "Back_Room"
        row = "BR12"
    elif(l == "BR13" or l == "1000010010100100011000100110011"):
        decode = "Back_Room"
        row = "BR13"
    elif(l == "BR21" or l == "1000010010100100011001000110001"):
        decode = "Back_Room"
        row = "BR21"
    elif(l == "BR22" or l == "1000010010100100011001000110010"):
        decode = "Back_Room"
        row = "BR22"
    elif(l == "BR23" or l == "1000010010100100011001000110011"):
        decode = "Back_Room"
        row = "BR23"
    elif(l == "BR31" or l == "1000010010100100011001100110001"):
        decode = "Back_Room"
        row = "BR31"
    elif(l == "BR31" or l == "1000010010100100011001100110001"):
        decode = "BR31"
        row = "Back_Room"
    elif(l == "BR32" or l == "1000010010100100011001100110010"):
        decode = "BR32"
        row = "Back_Room"
    elif(l == "BR33" or l == "1000010010100100011001100110011"):
        decode = "Back_Room"
        row = "BR33"
    elif(l == "DS00" or l == "1000100010100110011000000110000"):
        decode = "Dead_Stage"
        row = "DS00"
    else:
        print("Invalid Location. Enter a valid location!")
        decode = "Invalid"
        row = "Null"
        
    return decode, row