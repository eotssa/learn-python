# WRITE YOUR SOLUTION HERE:
class ListHelper:
    # returns the most common item on the list
    @classmethod
    def greatest_frequency(cls, my_list: list):
        get_set = set(my_list)


        freq_dict = {}
        for item in get_set:
            freq_dict[item] = my_list.count(item)
        
        return max(freq_dict, key=freq_dict.get)
        


    # returns the number of unique items which appear at least twice on the list
    @classmethod
    def doubles(cls, my_list: list):
        set_list = set([x for x in my_list if my_list.count(x) > 1]) 
        return len(set_list)




