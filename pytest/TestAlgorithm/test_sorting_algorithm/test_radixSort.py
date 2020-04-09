from radixSort import radix_sort
from randomListGenerator import small_random_list_generator, big_random_list_generator


# Sample test
def test_sample_list():
    sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    radix_sort(sorted_sample_list)
    # ordino sample_list con il metodo sort()
    sample_list.sort()
    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])


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
    sorted_list1 = list1.copy()
    sorted_list2 = list2.copy()
    sorted_list3 = list3.copy()
    # le ordino con counting sort
    radix_sort(sorted_list1)
    radix_sort(sorted_list2)
    radix_sort(sorted_list3)
    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1.sort()
    list2.sort()
    list3.sort()

    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])


# fixme: da togliere troppo tempo
def test_big_random_list():
    """
        Test su tre liste generate casualmente con un numero di elementi che varia da 11 a 22 con numeri che variano tra 1 e 100
    """
    # test liste create casualmente
    list1 = big_random_list_generator()
    list2 = big_random_list_generator()
    list3 = big_random_list_generator()

    # Copio le liste create che andrò ad ordinare con radix sort
    sorted_list1 = list1.copy()
    sorted_list2 = list2.copy()
    sorted_list3 = list3.copy()
    # le ordino con counting sort
    radix_sort(sorted_list1)
    radix_sort(sorted_list2)
    radix_sort(sorted_list3)
    # ordino le liste randomiche precedentemente create con il metodo sort()
    list1.sort()
    list2.sort()
    list3.sort()

    assert all([a == b for a, b in zip(list1, sorted_list1)])
    assert all([a == b for a, b in zip(list2, sorted_list2)])
    assert all([a == b for a, b in zip(list3, sorted_list3)])
