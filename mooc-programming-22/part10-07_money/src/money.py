# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"


    def __eq__(self, another: object): 
        return self.__str__() == another.__str__()
    
    def __lt__(self, another: object):
        if self.__euros == another.__euros:
            return self.__cents < another.__cents
        else:
            return self.__euros < another.__euros
    
    def __gt__(self, another: object):
        if self.__euros == another.__euros:
            return self.__cents > another.__cents
        else:
            return self.__euros > another.__euros

    def __ne__(self, another: object):
        return self.__str__() != another.__str__()


    def __add__(self, another: object):
        new_object = Money(0, 0)
        new_object.__euros = self.__euros + another.__euros
        new_object.__cents = self.__cents + another.__cents 

        if new_object.__cents >= 100: 
            new_object.__cents -= 100
            new_object.__euros += 1

        return new_object
    
    def __sub__(self, another: object):
        new_object = Money(0, 0)
        if (self.__euros - another.__euros < 0): 
            raise ValueError()
        new_object.__euros = self.__euros - another.__euros


        new_object.__cents = self.__cents - another.__cents
        
        if new_object.__cents < 0:
            if new_object.__euros - 1 < 0:
                raise ValueError
            else: 
                new_object.__euros -= 1
                new_object.__cents += 100


        return new_object


# <, > and !=.

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1