```python
# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = r"C:\Users\Wilson\AppData\Local\tmc\vscode\mooc-programming-22\part06-04_course_grading_part_1\src\students1.csv"
    exercise_data = r"C:\Users\Wilson\AppData\Local\tmc\vscode\mooc-programming-22\part06-04_course_grading_part_1\src\exercises1.csv"



students = {} 

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        # id, first, last
        students[parts[0]] = (parts[1] + " " +  parts[2]).strip() 

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue

        #id, exercise1 ... exercise7
        exercises[parts[0]] = parts[1:]  # returns a single string because [] is used for strings... 

sums = {} 

for key in exercises:
    #earlier [1:] implementation resulted in a string 
    grades = exercises[key] 
    grades = [int(grade) for grade in grades] # converts all string to int
    sums[key] = sum(grades)

#print(sums)

for pic, first_last in students.items():
    if pic in sums: 
        sum_grade = sums[pic]
        print(f"{first_last} {sum_grade}")

"""
there were some implementation issues with mine, such as using the string[:] functionality 
which caused issues down the road. important to know what they return. should look deeper. 
"""


"""model solution
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
 
students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(parts[i])
        exercises[parts[0]] = esum
 
for student_id, name in students.items():
    print(f"{name} {exercises[student_id]}")
"""
```


## my condensed revised ver. 

```python
exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue

        lst = [int(part) for part in parts[1:]] 
        #id, exercise1 ... exercise7
        exercises[parts[0]] = sum(lst)  # returns a single string because [] is used for strings... 

```