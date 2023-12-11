# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, accountNumber: int, balance: float) -> None:
        self.__owner = owner
        self.__accountNumber = accountNumber
        self.__balance = balance
    

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Negative Amount")
        
        self.__service_charge()


    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Overdrawn. Try again.")
        
        self.__service_charge()


    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        #self.balance is actually calling on the balance method... not the variable to reterive the balance
        one_percent = self.balance * 0.01
        self.__balance -= one_percent


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)