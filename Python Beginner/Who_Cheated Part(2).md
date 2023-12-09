
# Who cheated, version 2

**Points:** 1/1

You have the CSV files from the previous exercise at your disposal again. Please write a function named `final_points()`, which returns the final exam points received by the students, in a dictionary format, following these criteria:

- If there are multiple submissions for the same task, the submission with the highest number of points is taken into account.
- If the submission was made over 3 hours after the start time, the submission is ignored.
- The tasks are numbered 1 to 8, and each submission is graded with 0 to 6 points.

In the dictionary returned, the key should be the name of the student, and the value should be the total points received by the student.

Hint: Nested dictionaries might be a good approach when processing the tasks and submission times of each student.



```python
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

```

**BOTH MY SOLUTION AND IDEALIZED SOLUTION IS PRETTY MUCH THE SAME, NO DIFFERENCE IN METHOD. I WILL SAY INITIALIZING VARIABLES BEFOREHAND WITH PROPER NAMES DOES MAKE CODE MORE READABLE.  HE ALSO INITIALIZES A LOT OF OTHER ASPECTS AS WELL... **

#### Model Solution 

```python
import csv
from datetime import datetime, timedelta
 
def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student time and points is saved to a dictionary
        # Time and points is saved as tuple.
        points = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            tno = int(row[1])
            p = int(row[2])
            time = datetime.strptime(row[3], "%H:%M")
 
            # If cheating has happened, submission is not handled
            if time - start_times[name] > timedelta(hours=3):
                continue
 
            # If student is not handled yet, add student directly to the dictionary
            if name not in points:
                default_time = datetime(1900, 1, 1)
                points[name] = {}
                for i in range(1, 8+1):
                    points[name][i] = 0
                points[name][tno] = p
 
            # If student already exists, more points than earlier is required
            elif p > points[name][tno]:
                points[name][tno] = p
 
        final_points = {}
        # Iterate through students one by one
        for student in points:
            p = 0
            for exercise in points[student]:
                p += points[student][exercise]
            final_points[student] = p
 
        return final_points
 
# Write your solution here
```