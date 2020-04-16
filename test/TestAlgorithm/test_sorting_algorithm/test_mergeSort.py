# Test merge sort
from randomListGenerator import small_random_list_generator, big_random_list_generator
from mergeSort import merge_sort


def test_sample_list():
    """
        Test su una lista semplice
    """
    sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    merge_sort(sorted_sample_list, 0, len(sorted_sample_list))
    # ordino sample_list con il metodo sort()
    sample_list.sort()

    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])



def test_random_list():
    """
        Test su tre liste generate casualmente con un numero di elementi che varia da 11 a 22 con numeri che variano tra 1 e 100
    """
    list1 = small_random_list_generator()
    list2 = small_random_list_generator()
    list3 = small_random_list_generator()

    # copio le liste precedentemente create nell corrispettive sorted_list
    sorted_list1 = list1.copy()
    sorted_list2 = list2.copy()
    sorted_list3 = list3.copy()

    # le ordino con merge_sort
    merge_sort(sorted_list1, 0, len(sorted_list1))
    merge_sort(sorted_list2, 0, len(sorted_list2))
    merge_sort(sorted_list3, 0, len(sorted_list3))

    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1.sort()
    list2.sort()
    list3.sort()

    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])


def test_big_random_lists():
    """
        Test su tre liste generate casualmente con un numero di elementi che varia da 10000 a 100000
         con numeri che variano tra 1 e 100000
    """
    list1 = big_random_list_generator()
    list2 = big_random_list_generator()
    list3 = big_random_list_generator()

    # copio le liste precedentemente create nell corrispettive sorted_list
    sorted_list1 = list1.copy()
    sorted_list2 = list2.copy()
    sorted_list3 = list3.copy()

    # le ordino con merge_sort
    merge_sort(sorted_list1, 0, len(sorted_list1))
    merge_sort(sorted_list2, 0, len(sorted_list2))
    merge_sort(sorted_list3, 0, len(sorted_list3))

    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1.sort()
    list2.sort()
    list3.sort()

    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])
