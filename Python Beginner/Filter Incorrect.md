```python
def filter_incorrect():
    with open("lottery_numbers.csv", "r") as source_file, open("correct_numbers.csv", "w") as destination_file:
        for row in source_file:
            # remove new line character
            row = row.strip() 

            # (split weeks + #) and (the lottery numbers)
            parts = row.split(';')

            # checks for two parts
            if len(parts) != 2:
                continue

            # checks if weeks and number exists -- isdigit is okay with str 
            parts_week = parts[0].split(" ")           
            if len(parts_week) != 2 or not parts_week[1].isdigit() or not parts_week[0].lower() == "week": 
                continue

            # stores the lottery numbers in a list, only if it's actually numbers (and not ** or letters)
            numbers = [int(part) for part in parts[1].split(',') if part.isdigit()] 
            
            #dual functionality of part.isdigit(), solves for "One or more numbers are not correct:" and "len list"
            if len(numbers) != 7:
                continue

            # checks unique numbers
            unique_numbers = set(numbers)
            if len(unique_numbers) != 7:
                continue

            valid_nums = True
            for number in numbers: 
                if number < 1 or number > 39:
                    valid_nums = False
                    break
            
            if valid_nums: 
                destination_file.write(row + "\n")
                    
                




if __name__ == "__main__":
    filter_incorrect()

    """Model Solution uses more try, except structures to parse data, and invalid data is handled in the except block instead of timing out

    def filter_incorrect():
    with open("lottery_numbers.csv") as input_file, open("correct_numbers.csv", "w") as result_file:
        for row in input_file:
            parts = row.strip().split(";")
            if len(parts) != 2:
                continue
            week = parts[0].split(" ")
            error = False
            if len(week) != 2 or week[0] != "week":
                error = True
            try:
                mika = int(week[1])
            except:
                error = True
            number_list = parts[1].split(",")
            if len(number_list) != 7:
                error = True
 
            # numbers already listed --> to find out duplicates
            listed = []
            for item in number_list:
                try:
                    number = int(item)
                    if number < 1 or number > 39 or number in listed:
                        error = True
                    listed.append(number)
                except:
                    error = True
            if not error:
                result_file.write(row)
    """
```