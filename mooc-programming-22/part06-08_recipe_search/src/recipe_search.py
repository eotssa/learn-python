# Write your solution here
def open_file(filename: str) -> list:  
    this_lst = []
    this_lst.append("")
    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            this_lst.append(line)

    return this_lst


def search_by_name(filename: str, word: str): 
    this_lst = open_file(filename)

    return_lst = []
    for i in range(0, len(this_lst)):
        if this_lst[i] == "" and i <= len(this_lst):  #title always comes after "" 
            if this_lst[i+1].lower().find(word.lower()) != -1:
                return_lst.append(this_lst[i+1])
    
    return return_lst

def search_by_time(filename: str, prep_time: int):
    this_lst = open_file(filename)


    return_lst = []
    for i in range(0, len(this_lst)):
        if this_lst[i] == "" and int(this_lst[i + 2]) <= prep_time and (i + 2) <= len(this_lst):  
            return_lst.append(this_lst[i+1] + ", preparation time " + this_lst[i + 2] + " min")

    return return_lst

def search_by_ingredient(filename: str, ingredient: str):
    this_lst = open_file(filename)

    #is_Flag = True 
    return_lst = []
    for i in range(0, len(this_lst)):
        if this_lst[i] == "" and i <= len(this_lst):
            is_Title = True
            counter = i + 2 
            while is_Title and counter <= len(this_lst):
                if this_lst[counter] == "":
                    is_Title = False

                if ingredient.lower() == this_lst[counter].lower():
                    return_lst.append(this_lst[i+1] + ", preparation time " + this_lst[i + 2] + " min")
                    break
                
                counter += 1

    return return_lst


if __name__ == "__main__":

    found_recipes = search_by_ingredient("src/recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)


