# Write your solution here
import datetime

#ddmmyyXyyyz
def is_it_valid(pic: str) -> bool:
    
    if len(pic) != 11: 
        return False
    
    # + (1800s), - (1900s) or A (2000s).
    if pic[6] not in ["-", "+", "A"]:
        return False

    # solves the issue for ambigious datetime, since we only parse the xxXX years 
    dct = {}
    dct["+"] = "18"
    dct["-"] = "19"
    dct["A"] = "20"

    try: 
        #day, month, year for pic format --   ddmmyy 10 04 00
        #datetime format is year, month, day 
        is_valid = datetime.datetime(int(dct[pic[6]] + pic[4:6]), int(pic[2:4]), int(pic[:2]))
    except: 
        return False

    
    # nine-digit number created by the date of birth and the personal identifier

    try: 
        nine_digit = int(pic[0:6] + pic[7:10])
    except:
        #value error if not all digits
        return False
    remainder = nine_digit % 31 

    str_ident = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if pic[10] != str_ident[remainder]:
        return False
    
    return True

