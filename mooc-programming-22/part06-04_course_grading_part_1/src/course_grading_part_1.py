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

        lst = [int(part) for part in parts[1:]] 
        #id, exercise1 ... exercise7
        exercises[parts[0]] = sum(lst)  # returns a single string because [] is used for strings... 


for pic, first_last in students.items():
    if pic in exercises: 
        sum_grade = exercises[pic]
        print(f"{first_last} {sum_grade}")
