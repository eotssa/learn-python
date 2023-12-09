Sure, let's elaborate further on these concepts from a more advanced perspective.

**Class Variables**

Class variables are a part of class definition and are typically shared among all the instances of a class. If you want to maintain a piece of information that is shared by all objects, class variables are the way to go.

While instance variables are defined within methods (commonly within the `__init__` method), class variables are usually defined right after the class definition, and outside any methods.

Consider a scenario where you're creating a software for a bank that has a policy of changing the general interest rate for all savings accounts at once. This can be modeled using class variables as shown below:

```python
class SavingsAccount:
    general_interest_rate = 0.03  # class variable

    def __init__(self, account_number, balance, account_interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.account_interest_rate = account_interest_rate

    def calculate_interest(self):
        return self.balance * (SavingsAccount.general_interest_rate + self.account_interest_rate)

account1 = SavingsAccount("001", 1000, 0.01)
account2 = SavingsAccount("002", 2000, 0.02)

# Calculating interest
print(account1.calculate_interest())  # 40
print(account2.calculate_interest())  # 100
```

In the example above, `general_interest_rate` is a class variable. It is shared across all instances of the class `SavingsAccount`. 

**Class Methods**

Class methods are methods that are bound to the class and not the instance of the class. They can't modify the instance state (as they don't have access to `self`), but they can modify the class state (as they have access to `cls`, which is the class).

Class methods are defined with the `@classmethod` decorator and their first parameter is `cls` (instead of `self` for instance methods).

Consider a scenario where each savings account can have a different type of currency and we want a functionality to modify the default currency for all accounts:

```python
class SavingsAccount:
    default_currency = 'USD'  # class variable

    def __init__(self, account_number, balance, account_currency=None):
        self.account_number = account_number
        self.balance = balance
        self.account_currency = account_currency or SavingsAccount.default_currency

    @classmethod
    def change_default_currency(cls, new_currency):
        cls.default_currency = new_currency

account1 = SavingsAccount("001", 1000)  # Uses default currency 'USD'
account2 = SavingsAccount("002", 2000, 'EUR')  # Explicitly specifies 'EUR' as currency

# Changing default currency
SavingsAccount.change_default_currency('GBP')

account3 = SavingsAccount("003", 5000)  # Uses new default currency 'GBP'

print(account1.account_currency)  # USD
print(account2.account_currency)  # EUR
print(account3.account_currency)  # GBP
```

In the example above, `change_default_currency` is a class method that changes the class variable `default_currency`. This method can be called on the class (`SavingsAccount.change_default_currency('GBP')`) and it changes the value of `default_currency` for all instances of the class that don't explicitly specify their currency.

**Final Note**

A thorough understanding of class variables and class methods can be vital in designing object-oriented software. Class variables are used to define properties that should be shared among all instances of a class. Class methods, on the other hand, can change the state of the class itself and are not tied to any specific instance of the class.