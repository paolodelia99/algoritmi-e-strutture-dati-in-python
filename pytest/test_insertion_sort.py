import pytest
from ..mainPackage.SortingAlgorithms.insertionSort import insertion_sort

sample_list = [3,5,1,9,8,2]

# Test the the sample list 
def sample_test():
    assert sample_list.sort() == insertion_sort(sample_list)

# test random list 
list1 = []
list2 = []
list3 = []

for i in range(random.randint(10,22)):
    list1.append(random.randint(1,101))

for i in range(random.randint(10,22)):
    list2.append(random.randint(1,101))

for i in range(random.randint(10,22)):
    list3.append(random.randint(1,101))

def test_random_list():
    assert list1.sort() == insertion_sort(list1)
    assert list2.sort() == insertion_sort(list2)
    assert list3.sort() == insertion_sort(list3)