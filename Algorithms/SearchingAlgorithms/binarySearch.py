"""Binary Search 
Binary search is a recursive search algorithm, that finds an element in a ordere array

"""
import random

def binary_search(list,element):
    print(list)
    mid = len(list)//2
    if len(list) == 1 and element != list[mid]:
        return False
    elif element == list[mid]:
        return True
    elif element < list[mid]:
        return binary_search(list[0:mid],element)
    else:
        return binary_search(list[mid:len(list)],element)

# Default test
list = [1, 2, 3, 4, 5, 6, 8, 9, 10]

print(f'The initial list is {list}')
print('the element to find is 8')
if binary_search(list,8):
    print('8 is present in the list')
else: 
    print('8 isn\'t present in the list')

# Random Tests
list1 = []
list2 = []
list3 = []

for i in range(random.randint(10,22)):
    list1.append(random.randint(1,101))

for i in range(random.randint(10,22)):
    list2.append(random.randint(1,101))

for i in range(random.randint(10,22)):
    list3.append(random.randint(1,101))

# pick a random element in the lists
element1 = random.randint(1,101)
element2 = random.randint(1,101)
element3 = random.randint(1,101)

print(f'list number 1 is: {list1}')
if binary_search(list1,element1):
    print(f'{element1} is present in list number 1')
else:
    print(f'{element1} is not present in list number 1')

print(f'list number 2 is: {list2}')
if binary_search(list2,element2):
    print(f'{element2} is present in list number 2')
else:
    print(f'{element2} is not present in list number 2')

print(f'list number 3 is: {list3}')
if binary_search(list3,element3):
    print(f'{element3} is present in list number 3')
else:
    print(f'{element3} is not present in list number 3')