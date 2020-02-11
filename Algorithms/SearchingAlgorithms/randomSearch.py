"""Random Search Algorithm
The Random search algorithm is a search algorithm that find an element in a list
by choosing a random index every time until the all the indexes are choosen or when the
element is found

expected execution time: O(ln n) 
"""
import random

def random_search(list, element):
    counter_list = [0] * len(list)
    while not check_list_elements(counter_list):
        random_index = random.randint(0,len(list)-1)
        if list[random_index] == element:
            return True
        else:
            counter_list[random_index] = True
    
    return False


def check_list_elements(list):
    """Check if the list is made all by Trues
    
    Arguments:
        list {[bool]} -- list that stores old indexes choose by the random number
    
    Returns:
        bool -- if the list is made by all true returns true else false
    """
    for i in range(0,len(list)):
        if list[i] == False:
            return False
    
    return True

# Default List 
list = [34,43,20,11,1,84,98,44,76,64,16,35,12,77,2]

print(f'The initial list is: {list}')
if random_search(list,77):
    print('77 is present in the list')
else:
    print('77 is not present in the list')