# Write your solution here:
class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None

    def name(self):
        return self._name

    def numbers(self):
        return self._numbers

    def address(self):
        return self._address

    def add_number(self, number):
        self._numbers.append(number)

    def add_address(self, address):
        self._address = address

        
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name) # Person objects are stored inside dictionary 
        self.__persons[name].add_number(number)   # access person object, then call person.add_number

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    # should return list phone numbers from Person Object ?
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name] # currently returns Person object

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person == None: 
            print("number unknown")
            print("address unknown")
            return 
    
        if len(person.numbers()) == 0: # number is implemented as an empty list--not None?
            print("number unknown")
        else: 
            for number in person.numbers():
                print(number)       
        
        if person.address() == None:
            print("address unknown")
        else:
            print(person.address())  

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


application = PhoneBookApplication()
application.execute()

