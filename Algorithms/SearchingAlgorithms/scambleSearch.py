"""Scramble search

""" 
from deterministicSearch import deterministic_search
from randomizeInPlace import randomize_in_place

def scramble_search(list_,element):
    randomize_in_place(list_)
    if deterministic_search(list_,element):
        return True
    else:
        return False

# Default test
list_ = [34,43,20,11,1,84,98,44,76,64,16,35,12,77,2]
print(f'The initial list is {list_}')
if scramble_search(list_,84):
    print('84 is present in list')
else:
    print('84 is not present in list')