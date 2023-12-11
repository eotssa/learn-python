# Write your solution here
import urllib.request
import json

def retrieve_all():
    
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    my_data = (my_request.read()) # gets json data 

    data_read = json.loads(my_data)

    active_courses = []



    for course in data_read:
        if course['enabled'] == True:
            sum = 0
            for exercise in course['exercises']:
                sum += int(exercise)

            active_courses.append((course['fullName'], course['name'], course['year'], sum))


    return active_courses

def retrieve_course(course_name: str):
    courses = {} 
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats")
    my_data = (my_request.read()) # gets json data 

    data_read = json.loads(my_data)


    weeks = 0
    students = 0
    hours = 0
    exercises = 0
    #data_read is the entire dictionary object, say we just want to iterate over each key, then we would do data_read.values()
    for week in data_read.values(): 
        weeks += 1

        if int((week['students'])) > students:
            students = int(week['students'])
        

        hours += int(week['hour_total'])
        exercises += int(week['exercise_total'])

    #hour_average = hours divided by students value, rounded down 
    hour_average = hours // students

    #exercises_average: the exercises value divided by the students value (rounded down to the closest integer value)
    exercises_average = exercises // students

    courses['weeks'] = weeks
    courses['students'] = students
    courses['hours'] = hours
    courses['hours_average'] = hour_average
    courses['exercises'] = exercises
    courses['exercises_average'] = exercises_average

    return courses




if __name__ == "__main__":
    print(retrieve_course("docker2019"))