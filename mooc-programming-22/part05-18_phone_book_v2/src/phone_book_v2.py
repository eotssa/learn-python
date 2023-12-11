# Write your solution here
def search(my_dict : dict):
    name = input("name: ")
    if name in my_dict: 
        for item in my_dict[name]:  # prints out all values in a given key
            print(item)
    else:
        print("no number")    

def add(my_dict : dict): 
        name = input("name: ")
        number = input("number: ")
        # accomodate multiple numbers by storing list values 
        if name not in my_dict:
            my_dict[name] = []
    
        my_dict[name].append(number)
        print("ok!")

def main():
    my_dict = {}

    while True: 
        val = int(input("command (1 search, 2 add, 3 quit): "))
        if val == 1: 
            search(my_dict)
        elif val == 2: 
            add(my_dict)
        elif val == 3: 
            break

    print("quitting...")

main()
