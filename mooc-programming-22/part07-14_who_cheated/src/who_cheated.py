# Write your solution here
import csv
from datetime import datetime, timedelta, time

def cheaters():
    with open("start_times.csv") as file_one, open("submissions.csv") as file_two:
        students_start_time = {}
        # this line seperates elements into a list based on the delimiter 
        for line in csv.reader(file_one, delimiter=";"):
            students_start_time[line[0]] = datetime.strptime(line[1], "%H:%M").time()

        students_end_time = {}
        for line in csv.reader(file_two, delimiter=";"):
            if line[0] in students_end_time: 
                # checks if new_time is later than the current recorded time
                if datetime.strptime(line[3], "%H:%M").time() > students_end_time[line[0]]:
                    students_end_time[line[0]] = datetime.strptime(line[3], "%H:%M").time()
            #student name doesn't exist, add it 
            else:
                students_end_time[line[0]] = datetime.strptime(line[3], "%H:%M").time()

        #print(students_start_time)
        #print(students_end_time)

        cheaters_list = []
        for student in students_start_time:
            #time object can't subtract, convert to either datetime or timedelta object 
            end_time_delta = timedelta(hours=students_end_time[student].hour,
                                    minutes=students_end_time[student].minute)
            print("end_time_delta", end_time_delta)

            start_time_delta = timedelta(hours=students_start_time[student].hour, 
                                        minutes=students_start_time[student].minute)
        

            difference_time = end_time_delta - start_time_delta

            # 3 hour time_delta
            cut_off_time = timedelta(hours=3)

            if difference_time > cut_off_time:
                cheaters_list.append(student)

        return cheaters_list

