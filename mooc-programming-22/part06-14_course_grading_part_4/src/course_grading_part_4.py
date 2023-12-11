# write your solution here
if False: 
    student_info  = r"src\students1.csv"
    exercise_data = r"src\exercises1.csv"
    exam_data     = r"src\exam_points1.csv"
    course_info = r"src\course1.txt"
else: 
    student_info  = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data     = input("Exam points: ")
    course_info   = input("Course information: ")


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


exams = {}
with open(exam_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        
        # creates an integer list for each individual char in string parts[1:]
        lst = [int(part) for part in parts[1:]] 
        exams[parts[0]] = sum(lst)

def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]   # fixed: small logic error, adjusted to fit the lower bounds 
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i




course_lst = []
with open(course_info) as new_file:
    for line in new_file: 
        parts = line.split(':')
        course_lst.append(parts[1].strip())

with open("results.txt", "w") as my_file:
    my_file.write(f"{course_lst[0]}, {course_lst[1]} credits" + "\n")
    my_file.write("=" * 38 + "\n")
    my_file.write(f'{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}' + "\n")

    grade_dict = {} 
    for pic, first_last in students.items(): 
        if pic in exercises and pic in exams:
            #assuming total exercises is 40, and percentage of that rounded down 
            adjusted_exercise_points = int((exercises[pic] / 40) * 10)
            total_grade = exams[pic] + adjusted_exercise_points
            grade_dict[pic] = total_grade
            #print(f"{first_last} {grade(total_grade)}")
            my_file.write(f'{first_last:30}{exercises[pic]:<10}{adjusted_exercise_points:<10}{exams[pic]:<10}{total_grade:<10}{grade(total_grade):<10}' + "\n") # string are left aligned 

with open("results.csv", "w") as my_file:
    grade_dict = {} 
    for pic, first_last in students.items(): 
        if pic in exercises and pic in exams:
            #assuming total exercises is 40, and percentage of that rounded down 
            adjusted_exercise_points = int((exercises[pic] / 40) * 10)
            total_grade = exams[pic] + adjusted_exercise_points
            grade_dict[pic] = total_grade
            #print(f"{first_last} {grade(total_grade)}")
            my_file.write(f'{pic};{first_last};{grade(total_grade)}' + "\n") # string are left aligned 





print("Results written to files results.txt and results.csv")