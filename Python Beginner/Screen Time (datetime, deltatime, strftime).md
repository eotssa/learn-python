```
Programming exercise:
Screen time
Points:
0

---

Please write a program for recording the amount of time the user has spent in front of a television, computer, or mobile device screen over a specific period of time.

The program should work as follows:

Sample output:
Filename: late_june.txt
Starting date: 24.6.2020
How many days: 5
Please type in screen time in minutes on each day (TV computer mobile):
Screen time 24.06.2020: 60 120 0
Screen time 25.06.2020: 0 0 0
Screen time 26.06.2020: 180 0 0
Screen time 27.06.2020: 25 240 15
Screen time 28.06.2020: 45 90 5
Data stored in file late_june.txt

The user will input each day on a separate line, and the entries will contain three numbers separated by spaces, representing minutes.

With the above input, the program should store the data in a file named late_june.txt. The contents should look like this:

Sample data:
Time period: 24.06.2020-28.06.2020
Total minutes: 780
Average minutes: 156.0
24.06.2020: 60/120/0
25.06.2020: 0/0/0
26.06.2020: 180/0/0
27.06.2020: 25/240/15
28.06.2020: 45/90/5

```


```python
# Write your solution here
from datetime import datetime, timedelta

if False:
    file_name = "late_june.txt"
    start_date = "24.6.2020"
    num_days = 5
else:
    file_name = input("Filename: ")
    start_date = input("Starting date: ") # day, month, year 
    num_days = int(input("How many days: "))

# returns a datetime from parsed info
start_time = datetime.strptime(start_date, "%d.%m.%Y")

with open(file_name, "w") as new_file:
    print("Please type in screen time in minutes on each day (TV computer mobile):")

    days_to_add = timedelta(days=(num_days - 1))
    new_file.write(f"Time period: {start_time.strftime('%d.%m.%Y')}-{(start_time + days_to_add).strftime('%d.%m.%Y')}" + "\n")

    total_minutes = 0
    store_times = []
    for i in range(num_days):
        current_time = start_time + timedelta(days=i)
        inpt = input(f"Screen time {current_time}: ")
        
        #store times to write, due to formatting requirements--stored as string         
        store_times.append(inpt)


        parts = inpt.split(' ')
        for num in parts: 
            total_minutes += int(num)

    average_minutes = float(total_minutes) / float(num_days)
    new_file.write(f"Total minutes: {total_minutes}" + "\n")
    new_file.write(f"Average minutes: {average_minutes}" + "\n")


    for i in range(num_days):
        current_time = start_time + timedelta(days=i)
        new_file.write(f"{current_time.strftime('%d.%m.%Y')}: {store_times[i].replace(' ','/' )}" + "\n")
        
        

print(f"Data stored in file {file_name}")
```


##### Model Code...
```python
from datetime import datetime, timedelta
 
week = timedelta(days=7)
 
def format(aika):
    return aika.strftime("%d.%m.%Y")
 
file = input("Filename: ")
start = input("Starting date: ").split('.')
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")
 
screen_times = []
total = 0
start = datetime(int(start[2]), int(start[1]), int(start[0]))
 
for i in range(days):
    day = start + timedelta(days=i)
    times = input(f"Screen time {format(day)}: ").split(' ')
    tv = int(times[0])
    pc = int(times[1])
    mobile = int(times[2])
    total += tv + pc + mobile
    screen_times.append((day, tv, pc, mobile) )
 
with open(file, "w") as tdsto:
    tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
    tdsto.write(f"Total minutes: {total}\n")
    tdsto.write(f"Average minutes: {total/days:.1f}\n")
    for pv, tv, pc, mob in screen_times:
        tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")
 
print(f"Data stored in file {file}")
# Write your solution here

```