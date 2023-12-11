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