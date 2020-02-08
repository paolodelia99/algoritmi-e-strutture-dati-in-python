import random
"""
Bubble Sort


"""

def swap(list,first_index,second_index):
    tmp = list[first_index]
    list[first_index] = list[second_index]
    list[second_index] = tmp

def bubble_sort(list):
    for i in (0,len(list)-1):
        for j in range(len(list)-1,i,-1):
            if list[j] < list[i-1]:
                swap(list,j,i)

