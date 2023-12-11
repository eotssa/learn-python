# Write your solution here
import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))




# 12:00AM, 12/31/1999 is eve 
#datetime obj
eve_of_millennium = datetime.datetime(1999, 12, 31)

#datetime obj
born_time = datetime.datetime(year, month, day)

# datetime - datetime -> timedelta, then which we can access the days of timedelta 
days_old = (eve_of_millennium - born_time).days

#print(days_old)

if born_time > eve_of_millennium: 
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {days_old} days old on the eve of the new millennium.")