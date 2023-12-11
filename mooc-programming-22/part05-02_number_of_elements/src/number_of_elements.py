# Write your solution here
def count_matching_elements(my_matrix: list, element: int) -> int:
    counter = 0
    for row in my_matrix:
        for cell in row:
            if element == cell: 
                counter += 1
    
    return counter

