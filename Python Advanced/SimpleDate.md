```python
# WRITE YOUR SOLUTION HERE:

# assumes every month has 30 days, as such, do not use 'datetime' 
class SimpleDate:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def month(self):
        return self.__month
    
    @month.setter
    def month(self, month: int):
        if month >= 0 or month <= 12:
            self.__month = month
        else:
            raise ValueError("Invalid month")
        
    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day: int):
        if day >= 0 or day <= 30:
            self.__day = day
        else:
            raise ValueError("Invalid day")

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year: int):
        if year >= 0 or year <= 12:
            self.__year = year
        else:
            raise ValueError("Invalid year")

    def __str__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"
        
    # helper 
    def convert_date_to_days(self, date: object) -> int:
        return (date.month * 30) + (date.year * 360) + (date.day)

    # helper 
    def convert_days_to_date(self, days: int) -> object:
        years = days // 360
        months = (days - (years * 360)) // 30
        days = days - (years * 360) - (months * 30)

        return SimpleDate(days, months, years)

    # implement comparasion operators < > == != 
    def __lt__(self, another: object) -> bool:
        return self.convert_date_to_days(self) < self.convert_date_to_days(another)

    def __gt__(self, another: object) -> bool:
        return self.convert_date_to_days(self) > self.convert_date_to_days(another)

    def __eq__(self, another: object) -> bool:
        return self.convert_date_to_days(self) == self.convert_date_to_days(another)

    def __ne__(self, another: object) -> bool:
        return self.convert_date_to_days(self) != self.convert_date_to_days(another)
        

    def __add__(self, days: int) -> object:
        current_days = self.convert_date_to_days(self)
        current_days += days
        return self.convert_days_to_date(current_days)

    def __sub__ (self, another: "SimpleDate") -> int:
        return abs(self.convert_date_to_days(self) - self.convert_date_to_days(another))

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)
```