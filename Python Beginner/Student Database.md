```python
# Write your solution here
def print_student(students: dict, name: str):
    if name not in students: 
        print(f"{name}: no such person in the database")
    elif name in students:
        if students[name] == []: 
            print(f"{name}:")
            print(" no completed courses")
        else: 
            print(f"{name}:")
            print(f" {len(students[name])} completed courses:")
            for courses in students[name]:
                print(f"  {courses[0]} {courses[1]}")

            # average grade
            sum = 0
            for courses in students[name]:
                sum += courses[1]
            print(f" average grade {sum / len(students[name])}")

def add_student(students: dict, name: str ):
    if name not in students:
        students[name] = []

def add_course(students: dict, name: str, course_grade: tuple):
    if name not in students: 
        print(f"{name}: no such person in the database")
        return 
    
    # zero grade, don't add
    if course_grade[1] == 0: 
        return
    
    # checks for existing classes, and if grade is higher 
    for i, course in enumerate(students[name]): 
        if course_grade[0] == course[0]: 
            # grade should never be lowered
            if course_grade[1] > course[1]: 
                students[name][i] = course_grade
            return 
    
    # appends if first time 
    students[name].append(course_grade)



def summary(students: dict):
    #student number 
    print(f"students {len(students)}")

    max = 0
    name_max = "" 
    for person in students: # this alone prints out the key only 
        if len(students[person]) > max:
            max = len(students[person])
            name_max = person
    print(f"most courses completed {max} {name_max}")


    # average grade
    highest_average = 0
    highest_average_person = ""


    for person in students:
        sum = 0
        for courses in students[person]:
            sum += courses[1]
            average_grade =  sum / len(students[person])

        if average_grade > highest_average:
            highest_average = average_grade
            highest_average_person = person 
    print(f"best average grade {highest_average} {highest_average_person}")

    

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)


```