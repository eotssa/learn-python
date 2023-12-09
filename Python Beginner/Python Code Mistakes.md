### Original Code that didn't compile 
```python 
# Write your solution here
def calculate_grade(my_exam : list[int], my_exercise : list[int]):
    # exercise points is x / 10, range [0 - 100] 
    # exam points range [0 - 20]

    for num in my_exercise: 
        num = num // 10  # rounds down, integer division / or //? 

    # combine values using zip() 
    combined_points = []
    for num1, num2 in zip(my_exam, my_exercise):
        combined_points.append(num1 + num2)

    # need to account for the automatic fail of  < 10 points, use range based values instead?
    i = 0   # counter to track exam automatic fails, regardless of points
    grade_list = []                  # "pythonic" method instead of iterating each seperatly, we use count()? 
    for total_points in combined_points: 
        if my_exam[i] < 10: 
            grade_list.append(0)
            i += 1
            continue

        if total_points <= 14 or total_points >= 0:
            grade_list.append(0)
        elif total_points <= 17:
            grade_list.append(1)
        elif total_points <= 20:
            grade_list.append(2)
        elif total_points <= 23:
            grade_list.append(3)
        elif total_points <= 27:
            grade_list.append(4)
        elif total_points <= 30:
            grade_list.append(5)
        
        i += 1 
    
    print("Statistics:") # 1st print
    # calculate point average
    sum = 0
    for num in grade_list: 
        sum += num
    
    average = sum / len(grade_list)

    print(f"Points average: {average}")

    # calculate pass percentage
    students_passed = len(grade_list) - grade_list.count(0)
    pass_percentage = students_passed / len(grade_list)
    print(f"Pass percentage: {pass_percentage}")

    # show grade distribution, formatted
    sort_grade_list = sorted(grade_list)
    # reverse list
    sort_grade_list[::-1]

    print("Grade distribution:")
    for i in range(len(sort_grade_list), 0, -1): 
        print(f"  {i}: ", "*" * sort_grade_list.count(i))




    
def main():
    exam_points_list = []
    num_exercise_list = []

    while True: 
        user_input = input() 

        if user_input == "": 
            break

        ## given that we're limited to using in-book knowledge, use find()? 
        exam_score = int(user_input[0: user_input.find(" ")])
        exercise_score = int(user_input[user_input.find(" ") + 1:])# index + 1, splicing functionality

        exam_points_list.append(exam_score)
        num_exercise_list.append(exercise_score)

        calculate_grade(exam_points_list, num_exercise_list)
    
main()
```

## Issue #1 
```python
    for num in my_exercise: 
        num = num // 10  # rounds down, integer division / or //? 
```
- **`for` loops do not alter data as shown.** num is a temporary variable used to iterate through the structure. 
##### Solution to Issue #1 v_1
```python
    weighted_my_exercise_list = []
    for num in my_exercise: 
        weighted_my_exercise_list.append(num // 10)  # rounds down, integer 
```
- ended up creating a new list and storing the values in there
#### Solution to Issue #1 v_1 **(LIST COMPHRENSION)**
```python
 my_exercise = [num // 10 for num in my_exercise]
```
- This is an example of a **list comprehension**, which is a Python feature that provides a concise way to create lists based on existing lists (or other iterable objects).


## Issue #2 (code conciseness) 
```python
    i = 0   # counter to track exam automatic fails, regardless of points
    grade_list = []                  # "pythonic" method instead of iterating each seperatly, we use count()? 
    for total_points in combined_points: 
        if my_exam[i] < 10: 
            grade_list.append(0)
            i += 1
            continue

        if total_points <= 14 or total_points >= 0:
            grade_list.append(0)
        elif total_points <= 17:
            grade_list.append(1)
        elif total_points <= 20:
            grade_list.append(2)
        elif total_points <= 23:
            grade_list.append(3)
        elif total_points <= 27:
            grade_list.append(4)
        elif total_points <= 30:
            grade_list.append(5)
        
        i += 1 
```
- this is more of a `C++` way of handling code. 

#### Solution to Issue #2 (enumeration function)
```python
for i, total_points in enumerate(combined_points): 
        if my_exam[i] < 10: 
            grade_list.append(0)
            continue

        if total_points <= 14 or total_points >= 0:
            grade_list.append(0)
        elif total_points <= 17:
            grade_list.append(1)
        elif total_points <= 20:
            grade_list.append(2)
        elif total_points <= 23:
            grade_list.append(3)
        elif total_points <= 27:
            grade_list.append(4)
        elif total_points <= 30:
            grade_list.append(5)

```
 
`enumerate()` is a built-in Python function that allows you to loop over something and have an automatic counter. 

When you use `enumerate()`, it gives you two values for each iteration of the loop: the count (or index) and the value of the item at that index. 

So when you write `for i, total_points in enumerate(combined_points):`, the variable `i` is set to the index of the current item in the loop, and `total_points` is set to the value of the item at that index.

**In your original code, you maintained the index `i` manually by initializing `i = 0` before the loop and incrementing `i` with `i += 1` inside the loop. `enumerate()` does this for you automatically.**

Let's say `combined_points` is `[14, 15, 20, 25, 30]`. 

Here's what `i` and `total_points` would be on each iteration of the loop:

- On the first iteration, `i` would be `0` and `total_points` would be `14`.
- On the second iteration, `i` would be `1` and `total_points` would be `15`.
- And so on, until the end of the list.

**The benefit of using `enumerate()` is that it makes the code more readable and Pythonic (idiomatic Python). It's also safer in case you forget to increment `i`, and it's slightly more efficient because you're not performing an additional operation on each loop iteration.**

### Issue #3 (this loops over each element as opposed to each collection of unique grades)
```python
    for i in range(len(sort_grade_list), 0, -1): 
        print(f"  {i}: ", "*" * sort_grade_list.count(i))
```
- Issue: loops over each element, this is not what was intended. 
- Issue#2: Recall the use of range() and its parameters, we want to include grade "0", but that isn't included in the given parameters. 
#### Solution to Issue#3 V_1
```
   for i in range(5, -1, -1): # can use set() function to get unique set of grades, but not discussed. 
        print(f"  {i}:", "*" * sort_grade_list.count(i))
```
- Hard-coded the grading range (not ideal, but works)
- Fixed parameter to be -1, so that 0 is included.
#### **Solution to Issue#3 V_2 (better), use of `set()` function**
```python
   for i in range(len(set(grade_list)), 0, -1): 
        print(f"  {i}: ", "*" * grade_list.count(i))
```
**- set(grade_list) to get a collection of unique grades.** 

### Issue #4: return values on certain functions
```python
    # show grade distribution, formatted
    sort_grade_list = sorted(grade_list)
    # reverse list
    sort_grade_list[::-1]
```
- The list grade_list is reversed using [::-1], but this doesn't actually change grade_list itself, it just returns a reversed copy.
#### Solution to Issue#4
```
```

### Other Improvements #1 (using **split()** for multiple inputs) 
```python
exam_points_list = []
num_exercise_list = []

while True: 
    user_input = input("Exam points and exercises completed: ") 

    if user_input == "": 
        break

    user_input_list = user_input.split()

    exam_point = int(user_input_list[0])
    num_exercise = int(user_input_list[1])
    
    exam_points_list.append(exam_point)
    num_exercise_list.append(num_exercise)
```

In this revised code, the `split()` function creates a list of two strings from the user's input. The `int(user_input_list[0])` and `int(user_input_list[1])` lines then convert the first and second elements of that list to integers, respectively. The rest of the code is the same as in the previous example.


### Compiled Code (Passed All Tests)
```python
# Write your solution here
def calculate_grade(my_exam : list[int], my_exercise : list[int]):
    # exercise points is x / 10, range [0 - 100] 
    # exam points range [0 - 20]

    weighted_my_exercise_list = []
    for num in my_exercise: 
        weighted_my_exercise_list.append(num // 10)  # rounds down, integer division / or //? 

    #print(weighted_my_exercise_list)    
    # combine values using zip() 
    combined_points = []
    for num1, num2 in zip(my_exam, weighted_my_exercise_list):
        combined_points.append(num1 + num2)

    #print(combined_points)

    # need to account for the automatic fail of  < 10 points, use range based values instead?
    i = 0   # counter to track exam automatic fails, regardless of points
    grade_list = []                  # "pythonic" method instead of iterating each seperatly, we use count()? 
    for total_points in combined_points: 
        if my_exam[i] < 10: 
            grade_list.append(0)
            i += 1
            continue

        if total_points <= 14:
            grade_list.append(0)
        elif total_points <= 17:
            grade_list.append(1)
        elif total_points <= 20:
            grade_list.append(2)
        elif total_points <= 23:
            grade_list.append(3)
        elif total_points <= 27:
            grade_list.append(4)
        elif total_points <= 30:
            grade_list.append(5)
        
        i += 1 
    
    print("Statistics:") # 1st print
    # calculate point average
    sum = 0
    for num in combined_points: 
        sum += num
    
    average = sum / len(combined_points)
    #print("my_exam list", my_exam)
    #print("Length of grade list", len(grade_list))
    #print("Grade list values", grade_list)
    print(f"Points average: {average}")

    # calculate pass percentage
    students_passed = len(grade_list) - grade_list.count(0)
    pass_percentage = students_passed / len(grade_list)
    print(f"Pass percentage: {pass_percentage * 100:.1f}")

    # show grade distribution, formatted
    sort_grade_list = sorted(grade_list)
    # reverse list
    sort_grade_list = sort_grade_list[::-1]

    print("Grade distribution:")
    for i in range(5, -1, -1): # can use set() function to get unique set of grades, but not discussed. 
        print(f"  {i}:", "*" * sort_grade_list.count(i))




    
def main():
    exam_points_list = []
    num_exercise_list = []

    while True: 
        user_input = input() 

        if user_input == "": 
            break

        ## given that we're limited to using in-book knowledge, use find()? 
        exam_score = int(user_input[0: user_input.find(" ")])
        exercise_score = int(user_input[user_input.find(" ") + 1:])# index + 1, splicing functionality

        exam_points_list.append(exam_score)
        num_exercise_list.append(exercise_score)


    calculate_grade(exam_points_list, num_exercise_list)
    
main()
```

## Model Solution
- This solution and the way it solves problems was eye-opening.
```python
def exam_and_exercise_completed(inpt):
    space = inpt.find(" ")
    exam = int(inpt[:space])
    exercise = int(inpt[space+1:])
    return [exam, exercise]
 
def exercise_points(amount):
    return amount // 10
 
def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i
 
def mean(points):
    return sum(points) / len(points)
 
def main():
    points = []
    grades = [0] * 6
    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break
 
        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts
 
        points.append(total_points)
        grd = grade(total_points)
        if exam_and_exercises[0] < 10:
            grd = 0
        grades[grd] += 1
 
    pass_pros = 100 * (len(points) - grades[0]) / len(points)
 
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")
 
main()
 
```