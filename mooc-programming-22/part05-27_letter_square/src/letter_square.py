# Write your solution here
# 

inpt = int(input("Layers: "))
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

num_char = inpt * 2 - 1
my_string = alphabet[inpt - 1] * num_char

splice_index_start = 0
splice_index_end = num_char

in_char_counter = num_char - 2

my_list = []
my_list.append(my_string)
print(my_string)
for i in range(1, inpt): 
    holder_string_start = my_string[:i]
    holder_string_end = my_string[num_char - i:]
    my_string = holder_string_start + (alphabet[inpt - i - 1] * in_char_counter) + holder_string_end
    my_list.append(my_string)
    in_char_counter -= 2
    print(my_string)

for line in my_list[::-1][1:]: # reverse, then skip first line
    print(line)
