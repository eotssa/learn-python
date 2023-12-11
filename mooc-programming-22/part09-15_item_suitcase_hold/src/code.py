# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int = 0) -> None:
        self.__name = name     
        self.__weight = weight 

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"    

# pack Item(s) into Suitcase, keep track of weight 
class Suitcase:
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__current_weight = 0
        self.__things = []


    def add_item(self, item: Item):
        if item.weight() + self.__current_weight <= self.__max_weight:
            self.__things.append(item)
            self.__current_weight += item.weight()

    
    def print_items(self):
        for item in self.__things:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self.__things)

    def heaviest_item(self):
        if len(self.__things) == 0:
            return None

        return max(self.__things, key=lambda item_obj: item_obj.weight())


    def __str__(self) -> str:
        if len(self.__things) == 1: 
            return f"{len(self.__things)} item ({self.__current_weight} kg)"
        else:
            return f"{len(self.__things)} items ({self.__current_weight} kg)"


class CargoHold:
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__current_weight = 0
        self.__things = []

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.__current_weight <= self.__max_weight:
            self.__things.append(suitcase)
            self.__current_weight += suitcase.weight()    


    def print_items(self):
        for suitcase in self.__things:
            suitcase.print_items()

    def __str__(self) -> str:
        if len(self.__things) == 1:
                return f"{len(self.__things)} suitcase, space for {self.__max_weight - self.__current_weight} kg"    
        else:
            return f"{len(self.__things)} suitcases, space for {self.__max_weight - self.__current_weight} kg"    


if __name__ == "__main__":
    hold = CargoHold(100)
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    hold.add_suitcase(suitcase)
    print(hold)