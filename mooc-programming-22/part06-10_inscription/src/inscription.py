# Write your solution here

input1 = input("Whom should I sign this to: ")
input2 = input("Where shall I save it: ")

with open(input2, "w") as my_file:
    my_file.write(f"Hi {input1}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")