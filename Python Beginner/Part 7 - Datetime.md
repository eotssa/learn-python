# The datetime object

The Python `datetime` module provides functionalities for working with dates and times. One of the key components of this module is the `datetime` object, which represents a specific date and time.

## Obtaining the current date and time

To get the current date and time, you can use the `datetime.now()` function:

```python
from datetime import datetime

current_time = datetime.now()
print(current_time)
```

Output:
```
2023-06-19 12:30:45.123456
```

## Creating a datetime object

You can also create a `datetime` object for a specific date and time by providing the year, month, day, hour, minute, second, and microsecond values:

```python
from datetime import datetime

my_time = datetime(2021, 12, 24, 18, 30, 0)
print(my_time)
```

Output:
```
2021-12-24 18:30:00
```

If you don't provide the time components, the default time will be set to midnight (00:00:00).

## Accessing datetime components

You can access the individual components of a `datetime` object using the corresponding attributes:

```python
from datetime import datetime

my_time = datetime(1952, 12, 24)

print("Day:", my_time.day)
print("Month:", my_time.month)
print("Year:", my_time.year)
```

Output:
```
Day: 24
Month: 12
Year: 1952
```

## Comparing datetime objects

Datetime objects can be compared using the standard comparison operators, such as `<`, `>`, `==`, etc. This allows you to check if one date is before, after, or equal to another date:

```python
from datetime import datetime

time_now = datetime.now()
midsummer = datetime(2023, 6, 21)

if time_now < midsummer:
    print("It is not yet Midsummer")
elif time_now == midsummer:
    print("Happy Midsummer!")
elif time_now > midsummer:
    print("It is past Midsummer")
```

Output:
```
It is not yet Midsummer
```

## Calculating the difference between datetime objects

You can calculate the difference between two `datetime` objects using the subtraction operator. The result is a `timedelta` object representing the time difference:

```python
from datetime import datetime

time_now = datetime.now()
midsummer = datetime(2023, 6, 21)

difference = midsummer - time_now
print("Midsummer is", difference.days, "days away")
```

Output:
```
Midsummer is 2 days away
```

## Performing arithmetic operations with datetime objects

You can perform arithmetic operations involving `datetime` and `timedelta` objects. Adding a `timedelta` object to a `datetime` object results in a new `datetime` object:

```python
from datetime import datetime, timedelta

midsummer = datetime(2023, 6, 21)
one_week = timedelta(weeks=1)
week_from_date = midsummer + one_week

print("A week after Midsummer it will be", week_from_date)

long_time = timedelta(weeks=32, days=15)
print("32 weeks and 15 days after Midsummer it will be", midsummer + long_time)
```

Output:
```
A week after Midsummer it will be 2023-06-28 00:00:00
32 weeks and 15 days after Midsummer it will be 2024-02-05 00:00:00
```

## Conclusion

The `datetime` object in Python's `datetime` module allows you to work with dates and times effectively. You can obtain the current date and time, create custom datetime objects, compare dates, calculate differences, and perform arithmetic operations. Understanding and utilizing the `datetime` object is essential for working with time-related data and operations in Python.


# **Programming Exercise: How old**

Please write a program that asks the user for their date of birth and then prints out how old the user was on the eve of the new millennium. The program should ask for the day, month, and year separately and print out the age in days. Please refer to the examples below:

Sample Output:
```
Day: 10
Month: 9
Year: 1979
You were 7417 days old on the eve of the new millennium.
```

Sample Output:
```
Day: 28
Month: 3
Year: 2005
You weren't born yet on the eve of the new millennium.
```

You may assume that all day-month-year combinations given as arguments will be valid dates. That is, there will not be a date like February 31st.


```Python
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
```