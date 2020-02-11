# Test merge sort
import random
from mergeSort import merge_sort

sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
# copio sample list in sorted_sample_list
sorted_sample_list = sample_list.copy()
# la ordino
merge_sort(sorted_sample_list, 0, len(sorted_sample_list))
# ordino sample_list con il metodo sort()
sample_list.sort()


def test_sample_list():
    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])


# test liste create casualmente
list1 = []
list2 = []
list3 = []

for i in range(random.randint(10, 22)):
    list1.append(random.randint(1, 101))

for i in range(random.randint(10, 22)):
    list2.append(random.randint(1, 101))

for i in range(random.randint(10, 22)):
    list3.append(random.randint(1, 101))

# copio le liste precedentemente create nell corrispettive sorted_list
sorted_list1 = list1.copy()
sorted_list2 = list2.copy()
sorted_list3 = list3.copy()
# le ordino con merge_sort
merge_sort(sorted_list1,0,len(sorted_list1))
merge_sort(sorted_list2,0,len(sorted_list2))
merge_sort(sorted_list3,0,len(sorted_list3))
# ordino le liste randomiche precedentemente create con il metodo sort()
list1.sort()
list2.sort()
list3.sort()


def test_random_list():
    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])