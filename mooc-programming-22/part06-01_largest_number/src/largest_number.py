# write your solution here
def largest(): 
    with open("numbers.txt") as new_file:
        lst = [] 
        for line in new_file: 
            line = line.replace("\n", "") # removes new-line character 
            lst.append(int(line))
        

        return max(lst)

