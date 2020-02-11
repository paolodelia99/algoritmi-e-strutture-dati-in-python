"""Binary Search 
Binary search is a recursive search algorithm, that finds an element in a ordere array

"""
import random


def binary_search(list_, element):
    mid = len(list_) // 2
    if len(list_) == 1 and element != list_[mid]:
        return False
    elif element == list_[mid]:
        return True
    elif element < list_[mid]:
        return binary_search(list_[0:mid], element)
    else:
        return binary_search(list_[mid:len(list_)], element)