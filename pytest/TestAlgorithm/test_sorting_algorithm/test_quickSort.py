""" Test Quick sort"""
from quickSort import quicksort, randomize_quicksort
from random import randint

# test quicksort
sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
# copio sample list in sorted_sample_list
sorted_sample_list = sample_list.copy()
# la ordino
quicksort(sorted_sample_list, 0, len(sorted_sample_list) - 1)
# ordino sample_list con il metodo sort()
sample_list.sort()


def test_sample_list():
    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])


# test liste create casualmente
list1 = []
list2 = []
list3 = []

for i in range(randint(10, 22)):
    list1.append(randint(1, 101))

for i in range(randint(10, 22)):
    list2.append(randint(1, 101))

for i in range(randint(10, 22)):
    list3.append(randint(1, 101))

# copio le liste precedentemente create nell corrispettive sorted_list
sorted_list1 = list1.copy()
sorted_list2 = list2.copy()
sorted_list3 = list3.copy()
# le ordino con quicksort
quicksort(sorted_list1, 0, len(sorted_list1) - 1)
quicksort(sorted_list2, 0, len(sorted_list2) - 1)
quicksort(sorted_list3, 0, len(sorted_list3) - 1)
# ordino le liste randomiche precedentemente create con il metodo sort()
list1.sort()
list2.sort()
list3.sort()


def test_random_list():
    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])


""" Test random_quicksort (uso il postfisso ra)"""
sample_list_ra = [5, 2, 4, 7, 1, 3, 2, 6]
# copio sample list in sorted_sample_list
sorted_sample_list_ra = sample_list.copy()
# la ordino
randomize_quicksort(sorted_sample_list_ra, 0, len(sorted_sample_list_ra) - 1)
# ordino sample_list con il metodo sort()
sample_list_ra.sort()


def test_sample_list_random_algo():
    assert all([a == b for a, b in zip(sample_list_ra, sorted_sample_list_ra)])

# test liste create casualmente
list1_ra = []
list2_ra = []
list3_ra = []

for i in range(randint(10, 22)):
    list1_ra.append(randint(1, 101))

for i in range(randint(10, 22)):
    list2_ra.append(randint(1, 101))

for i in range(randint(10, 22)):
    list3_ra.append(randint(1, 101))

# copio le liste precedentemente create nell corrispettive sorted_list_ra
sorted_list1_ra = list1_ra.copy()
sorted_list2_ra = list2_ra.copy()
sorted_list3_ra = list3_ra.copy()
# le ordino con random_quicksort
quicksort(sorted_list1_ra, 0, len(sorted_list1_ra) - 1)
quicksort(sorted_list2_ra, 0, len(sorted_list2_ra) - 1)
quicksort(sorted_list3_ra, 0, len(sorted_list3_ra) - 1)
# ordino le liste randomiche precedentemente create con il metodo sort()
list1_ra.sort()
list2_ra.sort()
list3_ra.sort()


def test_random_list_random_algo():
    assert all([a == b for a, b in zip(list1_ra, sorted_list1_ra)])
    assert all([a == b for a, b in zip(list2_ra, sorted_list2_ra)])
    assert all([a == b for a, b in zip(list3_ra, sorted_list3_ra)])