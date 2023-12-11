# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'


class SuperGroup():
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []

    @property
    def location(self):
        return self._location
    
    @property
    def name(self):
        return self._name
    
    def add_member(self, superhero: SuperHero):
        self._members.append(superhero)
    
    def print_group(self):
        print(f"{self._name}, {self._location}")
        print("Members:")
        for member in self._members:
            print(f"{member.name}, superpowers: {member.superpowers}")

if __name__ == "__main__":

    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()