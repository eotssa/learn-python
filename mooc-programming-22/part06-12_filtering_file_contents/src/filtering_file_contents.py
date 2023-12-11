# Write your solution here
def filter_solutions(): 
    with open("solutions.csv", "r") as my_file:
        lst = []
        for row in my_file: 
            row = row.strip()
            parts = row.split(';')
            lst.append([parts[0], parts[1], parts[2]])
        #print(lst)

    with open("correct.csv", "w") as my_file:
        pass

    with open("incorrect.csv", "w") as my_file:
        pass


    for person in lst:
        if person[1].find("+") != -1:
            parts = person[1].split("+")
            if int(parts[0]) + int(parts[1]) == int(person[2]): 
                with open("correct.csv", "a") as my_file: 
                    my_file.write(f"{person[0]};{person[1]};{person[2]}" + "\n")
            else:
                with open("incorrect.csv", "a") as my_file: 
                    my_file.write(f"{person[0]};{person[1]};{person[2]}" + "\n")
        elif person[1].find("-") != -1:
            parts = person[1].split("-")
            if int(parts[0]) - int(parts[1]) == int(person[2]): 
                with open("correct.csv", "a") as my_file: 
                    my_file.write(f"{person[0]};{person[1]};{person[2]}" + "\n")
            else:
                with open("incorrect.csv", "a") as my_file: 
                    my_file.write(f"{person[0]};{person[1]};{person[2]}" + "\n")            



"""model solution
-- one thing to note is how all files are opened in one line, otherwise, nothing I didn't do, but neater. 



def filter_solutions():
    # Open all lines
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            # Split into pieces
            pieces = row.split(";")
 
            calculation = pieces[1]
            result = pieces[2]
 
            # Addition or subtraction?
            if "+" in calculation:
                operands = calculation.split("+")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands = calculation.split("-")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) - int(operands[1]) == int(result)
 
            # Write to file
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)

"""