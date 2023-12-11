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