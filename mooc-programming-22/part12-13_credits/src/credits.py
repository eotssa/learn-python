from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list):
    return reduce(lambda reduced_sum, attempt: reduced_sum + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    passed_attempts = filter(lambda attempt: attempt.grade >= 1, attempts)
    return reduce(lambda reduced_sum, attempt: reduced_sum + attempt.credits, passed_attempts, 0)

def average(attempts: list):
    # because I use passed_attempts twice, need to convert iter -> list otherwise the object is "used" after 1st go through. 
    passed_attempts = list(filter(lambda attempt: attempt.grade >= 1, attempts))
    total = reduce(lambda reduced_sum, attempt: reduced_sum + attempt.grade, passed_attempts, 0)
    num_courses = reduce(lambda reduced_sum, attempt: reduced_sum + 1, passed_attempts, 0)

    # print(total)
    # print(num_courses)
    return total / num_courses

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)


    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)


    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)