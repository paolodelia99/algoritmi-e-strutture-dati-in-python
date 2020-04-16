# Test selection sort
from randomListGenerator import small_random_list_generator, big_random_list_generator
from selectionSort import selecion_sort


def test_sample_list():
    """
        Test una sample list
    """
    sample_list = [4, 8, 2, 9, 10, 2, 5, 6, 1]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    selecion_sort(sorted_sample_list)
    # ordino sample_list con il metodo sort()
    sample_list.sort()
    assert sample_list.sort() == selecion_sort(sample_list)


def test_random_list():
    """
        Test su tre liste generate casualmente con un numero di elementi che varia da 11 a 22 con numeri che variano tra 1 e 100
    """
    # test liste create casualmente
    list1 = small_random_list_generator()
    list2 = small_random_list_generator()
    list3 = small_random_list_generator()

    # copio le liste precedentemente create nell corrispettive sorted_list
    sorted_list1 = list1.copy()
    sorted_list2 = list2.copy()
    sorted_list3 = list3.copy()
    # le ordino con selection_sort
    selecion_sort(sorted_list1)
    selecion_sort(sorted_list2)
    selecion_sort(sorted_list3)
    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1.sort()
    list2.sort()
    list3.sort()

    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])
