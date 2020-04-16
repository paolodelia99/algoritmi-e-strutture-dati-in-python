from countingSort import counting_sort
from randomListGenerator import small_random_list_generator, big_random_list_generator


# Sample test

def test_sample_list():
    sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    order_list = [0] * len(sample_list)
    counting_sort(sorted_sample_list, order_list, max(sample_list))
    # ordino sample_list con il metodo sort()
    sample_list.sort()
    assert all([a == b for a, b in zip(sample_list, order_list)])


def test_random_list():
    """
        Test su tre liste generate casualmente con un numero di elementi che varia da 11 a 22 con numeri che variano tra 1 e 100
    """
    # test liste create casualmente
    list1 = small_random_list_generator()
    list2 = small_random_list_generator()
    list3 = small_random_list_generator()

    # copio le liste precedentemente create nell corrispettive list_copy e creo
    # liste dove andranno a finire gli elementi ordinati
    list1_copy = list1.copy()
    sorted_list1 = [0] * len(list1_copy)
    list2_copy = list2.copy()
    sorted_list2 = [0] * len(list2_copy)
    list3_copy = list3.copy()
    sorted_list3 = [0] * len(list3_copy)
    # le ordino con counting sort
    counting_sort(list1_copy, sorted_list1, max(list1_copy))
    counting_sort(list2_copy, sorted_list2, max(list2_copy))
    counting_sort(list3_copy, sorted_list3, max(list3_copy))
    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1.sort()
    list2.sort()
    list3.sort()

    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])


def test_big_random_list():
    """
        Test su tre liste generate casualmente con un numero di elementi che varia tra 10000 e 100000 con numeri che variano tra 1 e 1000000
    """
    # test liste create casualmente
    list1 = big_random_list_generator()
    list2 = big_random_list_generator()
    list3 = big_random_list_generator()

    # copio le liste precedentemente create nell corrispettive list_copy e creo
    # liste dove andranno a finire gli elementi ordinati
    list1_copy = list1.copy()
    sorted_list1 = [0] * len(list1_copy)
    list2_copy = list2.copy()
    sorted_list2 = [0] * len(list2_copy)
    list3_copy = list3.copy()
    sorted_list3 = [0] * len(list3_copy)
    # le ordino con counting sort
    counting_sort(list1_copy, sorted_list1, max(list1_copy))
    counting_sort(list2_copy, sorted_list2, max(list2_copy))
    counting_sort(list3_copy, sorted_list3, max(list3_copy))
    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1.sort()
    list2.sort()
    list3.sort()

    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])