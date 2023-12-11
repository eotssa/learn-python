# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: "Person"):
        self.persons.append(person)
    
    # if empty, return True
    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        sum_height = sum([person.height for person in self.persons])
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum_height} cm")
        for person in self.persons:
            print(f"{person} ({person.height} cm)")

    # There has to be a better way...
    def shortest(self):
        if self.is_empty():
            return None

        shortest_person = min(self.persons, key=lambda person: person.height)
        return shortest_person
    
    def remove_shortest(self):
        if self.is_empty():
            return None

        for person in self.persons:
            if self.shortest().name == person.name:
                self.persons.remove(person)
                return person     
        
if __name__ == "__main__":

    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()   