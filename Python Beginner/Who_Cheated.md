# Who cheated

**Points:** 1/1

The file `start_times.csv` contains individual start times for a programming exam, in the format `name;hh:mm`. An example:

```
jarmo;09:00
timo;18:42
kalle;13:23
```

Additionally, the file `submissions.csv` contains points and hand-in times for individual exercises. The format here is `name;task;points;hh:mm`. An example:

```
jarmo;1;8;16:05
timo;2;10;21:22
jarmo;2;10;19:15
```

Your task is to find the students who spent over 3 hours on the exam tasks. That is, any student whose any task was handed in over 3 hours later than their exam start time is labeled a cheater. There may be more than one submission for the same task for each student. You may assume all times are within the same day.

Please write a function named `cheaters()`, which returns a list containing the names of the students who cheated.


### My Code 
- Issues: I used (time) instead of a datetime object, which forced to to later convert to timedelta or datetime, when I should've used datetime to begin with.
```python
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

```


### Model Code: just more clean, compare. 


```python
import csv
from datetime import datetime, timedelta
 
def cheaters():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        # First read students and start times to memory
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        # Then read submissions
        # From each student, last (i.e. greatest) is saved
        submission_times = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[3], "%H:%M")
            # If name does not exists in dictionary, add time directly to the dictionary
            if name not in submission_times:
                submission_times[name] = time
            # If there alredy exists time for key, compare if current time is greater
            elif time > submission_times[name]:
                submission_times[name] = time
        
        cheaters = []
        # Iterate through students one by one
        for name in start_times:
            if submission_times[name] - start_times[name] > timedelta(hours = 3):
                cheaters.append(name)
 
        return cheaters
```