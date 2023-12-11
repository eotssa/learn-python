# Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    inpt = int(input("Function: "))

    if inpt == 1: 
        inpt2 = input("Diary entry: ")
        with open("diary.txt", "a") as my_file: 
            my_file.write(inpt2)
            my_file.write("\n")
            print("Diary saved")
    
    if inpt == 2:
        with open("diary.txt", "r") as new_file:
            for line in new_file:
                print(line)

    if inpt == 0:
        break



print("Bye now!")

"""Looks like in the model code, instead of opening the file every time, 
the file is saved to a list after some text processing
then it both appends to the list and writes to a file to maintain the "read entries"


with open("diary.txt") as file:
    content = []
    for row in file:
        content.append(row.replace("\n",""))
 
# Open file for appending
with open("diary.txt", "a") as file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = input("Function: ")
        if function == "1":
            entry = input("Diary entry: ")
            file.write(entry + "\n")
            content.append(entry)
            print("Diary saved")
        elif function == "2":
            print("Entries:")
            for entry in content:
                print(entry)
        elif function == "0":
            print("Bye now!")
            break
"""