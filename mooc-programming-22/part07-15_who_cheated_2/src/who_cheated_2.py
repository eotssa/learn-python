# Write your solution here

# submissions
# name;task;points;hh:mm

# nested dictionaries
# name -> task -> grade 

import csv
from datetime import datetime, timedelta


def final_points():
    
    # stores student start time 
    with open("start_times.csv") as file_one:
            students_start_time = {}
            # this line separates elements into a list based on the delimiter 
            for line in csv.reader(file_one, delimiter=";"):
                students_start_time[line[0]] = datetime.strptime(line[1], "%H:%M")
    


    students_tasks = {}
    with open("start_times.csv") as file_one, open("submissions.csv") as file_two:
        for line in csv.reader(file_two, delimiter=";"):
            
            #If the submission was made over 3 hours after the start time, the submission is ignored.
            start_time = students_start_time[line[0]]
            task_end_time = datetime.strptime(line[3], "%H:%M")
            cut_off_time = timedelta(hours=3)

            if task_end_time - start_time > cut_off_time:
                continue

            # checks if a key exists, and creates both key-value pair
            if line[0] not in students_tasks:
                students_tasks[line[0]] = {}
                students_tasks[line[0]][line[1]] = int(line[2])
            # if key exists, checks if task is exists, if not, make one with score 
            elif line[0] in students_tasks:
                if line[1] not in students_tasks[line[0]]:
                    students_tasks[line[0]][line[1]] = int(line[2])
                # If there are multiple submissions for the same task, the submission with the highest number of points is taken into account.
                elif line[1] in students_tasks[line[0]]:
                    if int(line[2]) > int(students_tasks[line[0]][line[1]]):
                        students_tasks[line[0]][line[1]] = int(line[2])



    final_grade = {}
    for student in students_tasks:
        sum = 0
        for task in students_tasks[student]:
            sum += students_tasks[student][task]
 
        final_grade[student] = sum   

    return final_grade





if __name__ == "__main__":
    #print(cheaters())
    print(final_points())
