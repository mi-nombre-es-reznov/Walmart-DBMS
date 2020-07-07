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
    else:
        print("Invalid Location. Enter a valid location!")
        decode = "Invalid"
        row = "Null"
        
    return decode, row