# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)


def count_subordinates(employee: Employee):
    # returns 0 for any employee without underlings 
    if len(employee.subordinates) == 0:
        return 0

    # recursive case
    count = 0
    for subordinate in employee.subordinates:
        # 1 for the direct subordinate, plus their subordinates
        count += 1 + count_subordinates(subordinate)
    
    return count