"""Randomize in place

"""
from random import randint

def randomize_in_place(list_):
    n = len(list_)
    for i in range(0,n):
        random_index = randint(0,n-1)
        list_[i], list_[random_index] = list_[random_index], list_[i]

# Default Test
list1 = [144,55,66,12,85,74]
print(f'the initial list is {list1}')
randomize_in_place(list1)
print(f'the randomize list is {list1}')