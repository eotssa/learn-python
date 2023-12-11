def run(program):
    # Initialize the state of the program
    variables = {chr(i+65): 0 for i in range(26)}  # Variables A-Z
    pc = 0  # Program counter
    output = []  # Output list
    labels = {}  # Labels and their locations

    # Function to parse a value: either a number or a variable
    def parse_value(v):
        if v in variables:
            return variables[v]
        else:
            return int(v)

    # Function to evaluate a condition
    def eval_condition(cond):
        op1, comp, op2 = cond.split()
        op1 = parse_value(op1)
        op2 = parse_value(op2)
        if comp == "==":
            return op1 == op2
        elif comp == "!=":
            return op1 != op2
        elif comp == "<":
            return op1 < op2
        elif comp == "<=":
            return op1 <= op2
        elif comp == ">":
            return op1 > op2
        elif comp == ">=":
            return op1 >= op2

    # Find and store the locations of all labels
    for i, line in enumerate(program):
        if line.endswith(":"):
            labels[line[:-1]] = i

    # Start executing the program
    while pc < len(program):
        # Parse the line into command and operands
        parts = program[pc].split(maxsplit=1)
        command = parts[0]

        # Execute the command
        if command == "PRINT":
            value = parse_value(parts[1])
            output.append(value)
        elif command == "MOV":
            var, val = parts[1].split()
            variables[var] = parse_value(val)
        elif command == "ADD":
            var, val = parts[1].split()
            variables[var] += parse_value(val)
        elif command == "SUB":
            var, val = parts[1].split()
            variables[var] -= parse_value(val)
        elif command == "MUL":
            var, val = parts[1].split()
            variables[var] *= parse_value(val)
        elif command == "JUMP":
            pc = labels[parts[1]]
            continue
        elif command == "IF":
            condition, _, location = parts[1].partition(" JUMP ")
            if eval_condition(condition):
                pc = labels[location]
                continue
        elif command == "END":
            break

        # Go to the next line
        pc += 1

    # Return the output
    return output



"""model solution
def value(x, data):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x in characters:
        return data[characters.index(x)]
    else:
        return int(x)
 
def condition(a, condition, b):
    if condition == "==":
        return a == b
    if condition == "!=":
        return a != b
    if condition == "<":
        return a < b
    if condition == "<=":
        return a <= b
    if condition == ">":
        return a > b
    if condition == ">=":
        return a >= b
 
def run(program):
    length = len(program)
    row = 0
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    data = [0]*26
    result = []
    while True:
        if row == length:
            break
        parts = program[row].split(" ")
        if parts[0] == "PRINT   ":
            result.append(value(parts[1], data))
        if parts[0] == "MOV":
            data[characters.index(parts[1])] = value(parts[2], data)
        if parts[0] == "ADD":
            data[characters.index(parts[1])] += value(parts[2], data)
        if parts[0] == "SUB":
            data[characters.index(parts[1])] -= value(parts[2], data)
        if parts[0] == "MUL":
            data[characters.index(parts[1])] *= value(parts[2], data)
        if parts[0] == "JUMP":
            row = program.index(parts[1]+":")
            continue
        if parts[0] == "IF":
            if condition(value(parts[1], data), parts[2], value(parts[3], data)):
                row = program.index(parts[5]+":")
                continue
        if parts[0] == "END":
            break
        row += 1
    return result
"""