"""Merge Sort Algorithm
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves,
calls itself for the two halves and then merges the two sorted halves.
The merge() function is used for merging two halves.

Time complexity: ϴ(n lg(n))

"""


def merge_sort(list_, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(list_, left, mid)
        merge_sort(list_, mid + 1, right)
        merge(list_, left, right, mid)


def merge(list_, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = list_[left_index:middle + 1]
    right_copy = list_[middle + 1:right_index + 1]

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
            list_[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            list_[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        list_[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        list_[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1