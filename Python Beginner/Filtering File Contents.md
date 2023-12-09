```
The file solutions.csv contains some solutions to mathematics problems:

Arto;2+5;7
Pekka;3-2;1
Erkki;9+3;11
Arto;8-3;4
Pekka;5+5;10
...jne...
As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

Please write a function named filter_solutions() which

Reads the contents of the file solutions.csv
writes those lines which have a correct result into the file correct.csv
writes those lines which have an incorrect result into the file incorrect.csv
Using the example above, the file correct.csv would contain the lines

Arto;2+5;7
Pekka;3-2;1
Pekka;5+5;10
The other two would be in the file incorrect.csv.

Please write the lines in the same order as they appear in the original file. Do not change the original file.

NB: the function should have the exact same result, no matter how many times it is called. That is, it shouldn't matter if the function is called once

filter_solutions()
or multiple times in a row

filter_solutions()
filter_solutions()
filter_solutions()
filter_solutions()
After the execution, the contents of the files correct.csv and incorrect.csv should be exactly the same in either case.
```


```python
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
```


```solutions.csv
Kirka;79-15;22
Taina;84-24;60
Tony;75-15;60
Kirsi;86-22;32
Pekka;31+95;126
Mike;59-7;52
Pauli;82-6;43
Kirsi;27+12;39
Toni;70+47;117
Kirsi;69-50;40
Antti;91+84;175
Matti;67-41;26
Antti;65-39;26
Tiina;26+72;1
Tea;33+71;104
Pekka;97+53;150
Toni;34+71;66
Mike;1+6;61
Tony;48+66;114
Emilia;23+30;53
Tuula;99-42;57
Pauli;73-35;78
Paula;83-17;80
Kimmo;25+29;7
Kirka;92+47;56
Arto;26+81;107
Pauli;89-30;1
Antti;85+38;123
Toni;71-19;52
Pekka;34+67;101
Tiina;84+16;45
Toni;89-19;70
Tony;62+61;123
Pekka;90-25;65
Mike;63-12;77
Arto;73-20;17
Emilia;40+17;57
Tanja;92+77;169
Antti;36+95;131
Paula;81-33;48
Kirsi;88-41;47
Emilia;69+74;143
Juho;76-27;39
Juha;99-18;81
Paula;23+13;43
Antti;68-31;37
Tea;49+3;52
Juha;61-19;72
Kimmo;28+38;25
Tanja;10+26;47
Mia;34+79;113
Kirsi;62-1;91
Arto;76-27;75
Paula;94-11;83
Paula;85-48;45
Kirka;64+99;37
Pekka;55-26;29
Antti;66-25;19
Kimmo;98+13;45
Arto;71-23;39
Pekka;49+1;50
Tea;91+94;53
Tiina;68-27;53
Tiina;68-32;36
Kirsi;71-37;8
Mike;97-16;5
Paula;67-10;57
Kirsi;60+18;51
Mike;82+19;4
Lauri;86-21;65
Juho;95+26;30
Mia;93-27;38
Erkki;62-9;53
Matti;71-7;74
Arto;95+23;74
Matti;80-48;6
Pekka;68-44;22
Erkki;1+90;42
Matti;61+24;85
Tuula;61-37;85
Antti;37+64;5
Kirsi;74-47;85
Taina;16+43;24
Mia;51+36;87
Juho;21+38;83
Taina;62-33;10
Toni;52-7;45
Matti;59+2;20
Tiina;55-50;5
```