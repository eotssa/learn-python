# tee ratkaisusi tänne
class Course:
    def __init__(self, courseName: str) -> None:
        self.__courseName = courseName
        self.__grade = None
        self.__credit = None

    def courseName(self):
        return self.__courseName
    
    def grade(self):
        return self.__grade
    
    def credit(self):
        return self.__credit
    
    def add_grade(self, grade: int):
        if self.__grade == None: 
            self.__grade = grade
            return 
        
        # grade may be raised, but never lowered
        if self.__grade < grade:
            self.__grade = grade
    
    def add_credit(self, credit: int):
        self.__credit = credit

    def __str__(self) -> str:
        return f"{self.__courseName} ({self.__credit} cr) grade {self.__grade}"


class CourseRecords:
    def __init__(self) -> None:
        self.__courses = {}
        # self.__completed_courses = 0
        # self.__total_credits = 0
        # self.__grades = []


    def add_course(self, name: str, grade: int, credit: int):
        if not name in self.__courses:
            self.__courses[name] = Course(name)
            # self.__completed_courses += 1
            # self.__total_credits += credit

        
        self.__courses[name].add_grade(grade)
        # self.__grades.append(grade) # BIG ISSUE: if we try to add the same course 

        self.__courses[name].add_credit(credit)

    def get_course_data(self, name: str):
        if not name in self.__courses:
            return None
        
        # returns course object 
        return self.__courses[name] 
    

    def completed_courses(self) -> int:
        num_courses = 0
        for course in self.__courses:
            num_courses += 1
        
        return num_courses

    def mean(self): 
        total_grade = 0
        for key, value in self.__courses.items():
            total_grade += value.grade()

        mean = total_grade / self.completed_courses()
        return mean

    def generate_grade_list(self):
        lst = []
        for key, value in self.__courses.items():
            lst.append(value.grade())

        return lst

    def generate_credit_list(self):
        lst = []
        for key, value in self.__courses.items():
            lst.append(value.credit())

        return lst
    def statistics(self):
        if self.completed_courses() == 0: 
            mean = 0
        else:
            mean = self.mean()

        print(f"{self.completed_courses()} completed courses, a total of {sum(self.generate_credit_list())} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        for i in range (5, 0, -1):
            print("")
            print(f"{i}: ", end="")
            for grade in self.generate_grade_list():
                if grade == i: 
                    print("x", end="")
            

class CourseApplication:
    def __init__(self) -> None:
        self.__course = CourseRecords()

    def help(self): 
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credit: "))
        self.__course.add_course(name, grade, credits)

    def get_course_data(self):
        name = input("course: ")
        if self.__course.get_course_data(name) == None: 
            print("no entry for this course")
            return
        print(self.__course.get_course_data(name)) # this should work. It just returns the course, and follows the course obj __str__ method

    def statistics(self):
        self.__course.statistics()


    def execute(self):
        self.help() # runs interface format 
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3": 
                self.statistics()
            else:
                self.help()

application = CourseApplication()
application.execute()