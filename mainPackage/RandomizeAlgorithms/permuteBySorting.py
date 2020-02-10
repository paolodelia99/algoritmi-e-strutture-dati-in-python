"""Permute by sorting algorithm
Permute by sorting algorithm is randomize algorithm that create a new array with the same 
length as the input array and gives to each of its value a random number between 1 and n^3.
After that it creates a new permutation of the intial array using the P value as a order key
"""
from random import randint
import math

def permute_by_sorting(list_):
    n = len(list_)
    p_list = [0] * n
    # creates the random array
    for i in range(0,n):
        p_list[i] = randint(1,math.pow(n,3)+1)
    # creation of the tuple that has a first number the element 
    # of the first array and as a second number the number of the second list
    unorder_tuple = tuple(zip(list_,p_list))
    # sorted the tuple using the second element
    reorder_tuple = sorted(unorder_tuple, key=lambda x: x[1])
    # recopy back the items in the list 
    list_ = [item[0] for item in reorder_tuple]

    return list_


# Default test
list1 = [123,24,54,66]
print(f'the initial list is: {list1}')
permuted_list = permute_by_sorting(list1)
print(f'the final list is: {permuted_list}')
