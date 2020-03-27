""" Test Quick sort"""
from quickSort import quicksort, randomize_quicksort
from randomListGenerator import small_random_list_generator, big_random_list_generator


# test quicksort

def test_sample_list():
    sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    quicksort(sorted_sample_list, 0, len(sorted_sample_list) - 1)
    # ordino sample_list con il metodo sort()
    sample_list.sort()
    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])


def test_random_list():
    # test liste create casualmente
    list1 = small_random_list_generator()
    list2 = small_random_list_generator()
    list3 = small_random_list_generator()

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

    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])


# Test big random lists
def test_big_random_list():
    big_list_1 = big_random_list_generator()
    big_list_2 = big_random_list_generator()
    big_list_3 = big_random_list_generator()

    # copio le liste precedentemente create nell corrispettive sorted_list
    big_sorted_list1 = big_list_1.copy()
    big_sorted_list2 = big_list_2.copy()
    big_sorted_list3 = big_list_3.copy()

    # le ordino con quicksort
    quicksort(big_sorted_list1, 0, len(big_sorted_list1) - 1)
    quicksort(big_sorted_list2, 0, len(big_sorted_list2) - 1)
    quicksort(big_sorted_list3, 0, len(big_sorted_list3) - 1)

    # ordino le liste randomiche precedentemente create con il metodo sort()
    big_list_1.sort()
    big_list_2.sort()
    big_list_3.sort()

    assert all([a == b for a, b in zip(big_list_1, big_sorted_list1)])
    assert all([a == b for a, b in zip(big_list_2, big_sorted_list2)])
    assert all([a == b for a, b in zip(big_list_3, big_sorted_list3)])


""" Test random_quicksort (uso il postfisso ra)"""


def test_sample_list_random_algo():
    sample_list_ra = [5, 2, 4, 7, 1, 3, 2, 6]
    # copio sample list in sorted_sample_list
    sorted_sample_list_ra = sample_list.copy()
    # la ordino
    randomize_quicksort(sorted_sample_list_ra, 0, len(sorted_sample_list_ra) - 1)
    # ordino sample_list con il metodo sort()
    sample_list_ra.sort()
    assert all([a == b for a, b in zip(sample_list_ra, sorted_sample_list_ra)])


def test_random_list_random_algo():
    # test liste create casualmente
    list1_ra = small_random_list_generator()
    list2_ra = small_random_list_generator()
    list3_ra = small_random_list_generator()

    # copio le liste precedentemente create nell corrispettive sorted_list_ra
    sorted_list1_ra = list1_ra.copy()
    sorted_list2_ra = list2_ra.copy()
    sorted_list3_ra = list3_ra.copy()

    # le ordino con random_quicksort
    randomize_quicksort(sorted_list1_ra, 0, len(sorted_list1_ra) - 1)
    randomize_quicksort(sorted_list2_ra, 0, len(sorted_list2_ra) - 1)
    randomize_quicksort(sorted_list3_ra, 0, len(sorted_list3_ra) - 1)

    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1_ra.sort()
    list2_ra.sort()
    list3_ra.sort()

    assert all([a == b for a, b in zip(list1_ra, sorted_list1_ra)])
    assert all([a == b for a, b in zip(list2_ra, sorted_list2_ra)])
    assert all([a == b for a, b in zip(list3_ra, sorted_list3_ra)])


# Test big random lists
def test_big_random_list_random_algo():
    big_list_1 = big_random_list_generator()
    big_list_2 = big_random_list_generator()
    big_list_3 = big_random_list_generator()

    # copio le liste precedentemente create nell corrispettive sorted_list
    big_sorted_list1 = big_list_1.copy()
    big_sorted_list2 = big_list_2.copy()
    big_sorted_list3 = big_list_3.copy()

    # le ordino con quicksort
    randomize_quicksort(big_sorted_list1, 0, len(big_sorted_list1) - 1)
    randomize_quicksort(big_sorted_list2, 0, len(big_sorted_list2) - 1)
    randomize_quicksort(big_sorted_list3, 0, len(big_sorted_list3) - 1)

    # ordino le liste randomiche precedentemente create con il metodo sort()
    big_list_1.sort()
    big_list_2.sort()
    big_list_3.sort()

    assert all([a == b for a, b in zip(big_list_1, big_sorted_list1)])
    assert all([a == b for a, b in zip(big_list_2, big_sorted_list2)])
    assert all([a == b for a, b in zip(big_list_3, big_sorted_list3)])
