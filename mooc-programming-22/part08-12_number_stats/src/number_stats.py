# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.sum

    def average(self):
        if self.numbers == 0:
            return

        return (self.sum) / (self.numbers)

stats = NumberStats()
odd_stats = NumberStats()
even_stats = NumberStats()

while True:
    user_input = int(input("Please type in integer numbers: "))
    
    if user_input == -1: 
        break 

    if user_input % 2 == 0:
        even_stats.add_number(user_input)
    else:
        odd_stats.add_number(user_input)

    stats.add_number(user_input)




print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even_stats.get_sum())
print("Sum of odd numbers:", odd_stats.get_sum())
