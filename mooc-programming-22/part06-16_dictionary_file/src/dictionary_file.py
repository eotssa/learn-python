# Write your solution here

dct = {} 
with open("dictionary.txt", "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split('-') #splits to finnish, english
        dct[parts[0]] = parts[1] 
        #dct[parts[1]] = parts[0]

    
while True: 
    print("1 - Add word, 2 - Search, 3 - Quit")
    val = int(input("Function: "))


    if val == 1: 
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        
        #stores word in dictionary 
        dct[finnish] = english
        #dct[english] = finnish


        with open("dictionary.txt", "a") as my_file:
            my_file.write(f"{finnish} - {english}" + "\n")
    
        print("Dictionary entry added")

    if val == 2:
        search_term = input("Search term: ")
        
        with open("dictionary.txt", "r") as my_file:
            for row in my_file:
                if search_term in row: 
                    print(row)


    if val == 3: 
        break

print("Bye!")

