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
