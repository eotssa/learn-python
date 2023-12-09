This section explains handling dates and times in Python, and it introduces several key functionalities:

1. **datetime object**: The Python `datetime` module includes the `now` function which returns a datetime object containing the current date and time.

```python
from datetime import datetime
my_time = datetime.now()
print(my_time)
```
You can also create the datetime object yourself:

```python
from datetime import datetime
my_time = datetime(1952, 12, 24)
print(my_time)
```

2. **Accessing elements of datetime object**: You can access different elements of a datetime object, like the day, month, and year.

```python
from datetime import datetime
my_time = datetime(1952, 12, 24)
print("Day:", my_time.day)
print("Month:", my_time.month)
print("Year:", my_time.year)
```

3. **Time of day**: You can also specify the time of day when creating a datetime object. 

```python
from datetime import datetime
pv1 = datetime(2021, 6, 30, 13)     # 30.6.2021 at 1PM
pv2 = datetime(2021, 6, 30, 18, 45) # 30.6.2021 at 6.45PM
```

4. **Comparison and calculation of differences between datetime objects**: The familiar comparison operators also work on datetime objects.

```python
from datetime import datetime
time_now = datetime.now()
midsummer = datetime(2021, 6, 26)

if time_now < midsummer:
    print("It is not yet Midsummer")
elif time_now == midsummer:
    print("Happy Midsummer!")
elif time_now > midsummer:
    print("It is past Midsummer")
```
The difference between two datetime objects can be calculated simply with the subtraction operator:

```python
from datetime import datetime
time_now = datetime.now()
midsummer = datetime(2021, 6, 26)

difference = midsummer - time_now
print("Midsummer is", difference.days, "days away")
```

5. **Datetime and timedelta**: Addition is available between datetime and timedelta objects. 

```python
from datetime import datetime, timedelta
midsummer = datetime(2021, 6, 26)

one_week = timedelta(days=7)
week_from_date = midsummer + one_week

print("A week after Midsummer it will be", week_from_date)

long_time = timedelta(weeks=32, days=15)

print("32 weeks and 15 days after Midsummer it will be", midsummer + long_time)
```

6. **strftime method**: The `strftime` method allows you to format the string representation of a datetime object. 

```python
from datetime import datetime
my_time = datetime.now()
print(my_time.strftime("%d.%m.%Y"))
print(my_time.strftime("%d/%m/%Y %H:%M"))
```

7. **strptime function**: The `strptime` function parses a datetime object from a string given by the user. 

```python
from datetime import datetime
birthday = input("Please type in your birthday in the format dd.mm.yyyy: ")
my_time = datetime.strptime(birthday, "%d.%m.%Y")

if my_time < datetime(2000, 1, 1):
    print("You were born in the previous millennium")
else:
    print("You were born during this millennium")
```

```
Notation	Significance
%d	day (01–31)
%m	month (01–12)
%Y	year in 4 digit format
%H	hours in 24 hour format
%M	minutes (00–59)
%S	seconds (00–59)
```