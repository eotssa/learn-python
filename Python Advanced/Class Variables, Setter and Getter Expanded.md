```python
class PhoneNumber:
    country_codes = {"Finland": "+358", "Sweden": "+46", "United States": "+1"}
    
    def __init__(self, name: str, phone_number: str, country: str):
        self.__name = name
        # This is a call to the phone_number.setter method. self.__phone_number is init after checks 
        self.phone_number = phone_number
        # This is a call to the country.setter method, self.__country variable is init after checks
        self.country = country
    
    # self.__name setter and getter
    @property
    def name (self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    # self.__phone_number setter and getter
    @property
    def phone_number(self):
        # the initial zero is removed as the country code is prefixed
        return PhoneNumber.country_codes[self.__country] + " " + self.__phone_number[1:]
    
    @phone_number.setter
    def phone_number(self, phone_number: str):
        # checks if number has valid characters
        for num in phone_number:
            if num not in "1234567890 ":
                raise ValueError("A phone number can only contain numbers and spaces")
        self.__phone_number = phone_number
    

    # self.__country setter and getter
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, country: str):
        # checks if country is a key in country_codes (dictionary)
        if country not in PhoneNumber.country_codes:
            raise ValueError("This country is not on the list")
        self.__country = country


    # returns a phone_number without country codes
    @property
    def local_number(self):
        return self.__phone_number

    # note the difference between calling {self.__phone_number} (variable itself) vs {self.phone_number} (getter method)
    def __str__(self):
        return f"{self.phone_number} ({self.__name})"

if __name__ == "__main__":
    pn = PhoneNumber("Peter Pythons", "040 111 1111", "Sweden")
    print(pn)
    print(pn.phone_number)
    print(pn.local_number)
```