from bucketSort import bucket_sort
from randomListGenerator import zero_one_random_list_generator


def test_sample_list():
    """
        Sample test
    """
    sample_list = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.255, 0.723]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    sorted_sample_list = bucket_sort(sorted_sample_list, 10)
    # ordino sample_list con il metodo sort()
    sample_list.sort()
    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])


def test_small_random_list():
    """
        Testo bucket sort con liste di 20 elementi generate casualmente
    """
    # Creo tre liste di venti elementi generate casualmente
    list_1 = zero_one_random_list_generator(20)
    list_2 = zero_one_random_list_generator(20)
    list_3 = zero_one_random_list_generator(20)
    # Le copio nelle corrispettive sorted_list che verrano ordinate da bucket sort
    sorted_list_1 = list_1.copy()
    sorted_list_2 = list_2.copy()
    sorted_list_3 = list_3.copy()
    # le ordino con bucket sort
    sorted_list_1 = bucket_sort(sorted_list_1, 10)
    sorted_list_2 = bucket_sort(sorted_list_2, 10)
    sorted_list_3 = bucket_sort(sorted_list_3, 10)
    # ordino le liste iniziali
    list_1.sort()
    list_2.sort()
    list_3.sort()
    assert all([a == b for a, b in zip(list_1, sorted_list_1)])
    assert all([a == b for a, b in zip(list_2, sorted_list_2)])
    assert all([a == b for a, b in zip(list_3, sorted_list_3)])


def test_big_random_list():
    """
        Testo bucket sort con liste di 100000 elementi generate casualmente
    """
    # Creo tre liste di venti elementi generate casualmente
    list_1 = zero_one_random_list_generator(100000)
    list_2 = zero_one_random_list_generator(100000)
    list_3 = zero_one_random_list_generator(100000)
    # Le copio nelle corrispettive sorted_list che verrano ordinate da bucket sort
    sorted_list_1 = list_1.copy()
    sorted_list_2 = list_2.copy()
    sorted_list_3 = list_3.copy()
    # le ordino con bucket sort
    sorted_list_1 = bucket_sort(sorted_list_1, 10000)
    sorted_list_2 = bucket_sort(sorted_list_2, 10000)
    sorted_list_3 = bucket_sort(sorted_list_3, 10000)
    # ordino le liste iniziali
    list_1.sort()
    list_2.sort()
    list_3.sort()
    assert all([a == b for a, b in zip(list_1, sorted_list_1)])
    assert all([a == b for a, b in zip(list_2, sorted_list_2)])
    assert all([a == b for a, b in zip(list_3, sorted_list_3)])
