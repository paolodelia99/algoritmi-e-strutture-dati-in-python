# Testing Bubble Sort
from bubbleSort import bubble_sort
from randomListGenerator import small_random_list_generator


def sample_test():
    # default list
    sample_list = [4, 8, 2, 9, 10, 2, 5, 6, 1]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    bubble_sort(sorted_sample_list)
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

    # le ordino con bubble_sort
    bubble_sort(sorted_list1)
    bubble_sort(sorted_list2)
    bubble_sort(sorted_list3)

    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1.sort()
    list2.sort()
    list3.sort()
    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])
