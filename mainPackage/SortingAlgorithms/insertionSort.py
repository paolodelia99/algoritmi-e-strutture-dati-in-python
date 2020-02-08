import random, sys
"""Insertion Sort 

"""

def insertion_sort(list):
    for j in range(1,len(list)):

        key = list[j]
        i = j-1

        while i>=0 and list[i]>key:

            list[i+1] = list[i]
            i = i-1

        list[i+1] = key 

# Default list 
list = [25,36,85,4,56,95,22,65,45,87,31,2,15]
print(f'The default list: {list}')
insertion_sort(list)
print(f'The ordered list is: {list}')

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
insertion_sort(list1)
print(list1)

print('List n2:')
print(list2)
print('sorted list 2:')
insertion_sort(list2)
print(list2)

print('List n3: ')
print(list3)
print('sorted list 2:')
insertion_sort(list3)
print(list3)

sys.modules[__name__] = insertion_sort