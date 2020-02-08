import random
"""Merge Sort Algorithm
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves,
calls itself for the two halves and then merges the two sorted halves.
The merge() function is used for merging two halves.

Time complexity: ϴ(n lg(n))

"""
def merge_sort(list,left,right):
    if left < right:
        mid = (left+right)//2
        merge_sort(list,left,mid)
        merge_sort(list,mid+1,right)
        merge(list,left,right,mid)

def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
    
    
#default list
defaultList = [5,2,4,7,1,3,2,6]
print('The default list is:')
print(defaultList)
merge_sort(defaultList,0,len(defaultList)-1)
print(defaultList)

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
merge_sort(list1,0,len(list1)-1)
print(list1)

print('List n2:')
print(list2)
print('sorted list 1:')
merge_sort(list1,0,len(list1)-1)
print(list1)

print('List n3: ')
print(list3)
print('sorted list 1:')
merge_sort(list1,0,len(list1)-1)
print(list1)