# write your solution here

def read_fruits(): 
    with open("fruits.csv") as new_file: 
        this_dict = {}
        for line in new_file: 
            line = line.replace("\n", "") # removes space char 
            parts = line.split(";")       # returns a list seperated 
            fruit_name = parts[0]
            fruit_price = float(parts[1]) # forgot the (float)... 

            if fruit_name not in this_dict:
                this_dict[fruit_name]= fruit_price
    
    return this_dict