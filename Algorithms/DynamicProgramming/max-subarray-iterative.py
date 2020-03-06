import random

""" 
Kandane's Algorithm
Implementation of the iterative algorithm that finds the max sub array

"""
list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


def max_subarray(numbers):
    """

    """
    best_sum = 0
    best_start = best_end = 0
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the exsting sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1

    return dict({'bestSum': best_sum, 'bestStart': best_start, 'bestEnd': best_end})


# Check if it works for the default list
print('Default list: ')
print(list)
print(max_subarray(list))

# Test with three different Random list
list1 = []
list2 = []
list3 = []

for i in range(random.randint(10, 22)):
    list1.append(random.randint(-101, 101))

for i in range(random.randint(10, 22)):
    list2.append(random.randint(-101, 101))

for i in range(random.randint(10, 22)):
    list3.append(random.randint(-101, 101))

# Check if is working also with the random lists
print('Random Lists')
print('List n1:')
print(list1)
print('max subArray in list 1:')
print(max_subarray(list1))

print('List n2:')
print(list2)
print('max subArray in list 3:')
print(max_subarray(list2))

print('List n3: ')
print(list3)
print('max subArray in list 3:')
print(max_subarray(list3))
