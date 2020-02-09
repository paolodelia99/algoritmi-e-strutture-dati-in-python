import random
"""Bubble Sort

Bubble sort is an in-place comparison algorithm.
is a simple sorting algorithm that repeatedly steps through the list, 
compares adjacent elements and swaps them if they are in the wrong order.

Time complezity: O(n^2)
"""

def swap(list,first_index,second_index):
    tmp = list[first_index]
    list[first_index] = list[second_index]
    list[second_index] = tmp

def bubble_sort(list):
    """Bubble sort algorithm
    
    Arguments:
        list {[int]} -- list of unsorted numbers
    """
    for i in range(0,len(list)-1):
        for j in range(len(list)-1,i,-1):
            if list[j] < list[j-1]:
                swap(list,j,j-1)

# default list
list = [4,8,2,9,10,2,5,6,1]
print(f'initial list {list}')
bubble_sort(list)
print(f'sorted list: {list} ')

# random lists
# Test with three different Random list
list1 = []
list2 = []
list3 = []

for i in range(random.randint(10,22)):
    list1.append(random.randint(1,101))

for i in range(random.randint(10,22)):
    list2.append(random.randint(1,101))

for i in range(random.randint(10,22)):
    list3.append(random.randint(1,101))

#Check if is working also with the random lists
print('Random Lists')
print('List n1:')
print(list1)
print('sorted list 1:')
bubble_sort(list1)
print(list1)

print('List n2:')
print(list2)
print('sorted list 2:')
bubble_sort(list2)
print(list2)

print('List n3: ')
print(list3)
print('sorted list 2:')
bubble_sort(list3)
print(list3)
