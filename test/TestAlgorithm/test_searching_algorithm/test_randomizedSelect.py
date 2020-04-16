from random import randint
from randomSelect import randomized_select
from randomListGenerator import random_list_generator


def test_sample_list():
    """
        Sample test
    """
    arr = random_list_generator(10, 0, 20)
    ith_order_statistic = randomized_select(arr, 0, len(arr) - 1, 5)
    arr.sort()
    assert ith_order_statistic == arr[5 - 1]


def test_small_random_list():
    """
        Test con liste generate casualmente di 50 elementi con numeri che vanno da 0 a 100
    """
    list_1 = random_list_generator(50, 0, 100)
    list_2 = random_list_generator(50, 0, 100)
    list_3 = random_list_generator(50, 0, 100)

    # numeri casuali
    random_1 = randint(0, 50)
    random_2 = randint(0, 50)
    random_3 = randint(0, 50)

    # statistiche d'ordine con i numeri casuali trovati precedentemente
    ith_order_statistic_1 = randomized_select(list_1, 0, len(list_1) - 1, random_1)
    ith_order_statistic_2 = randomized_select(list_2, 0, len(list_2) - 1, random_2)
    ith_order_statistic_3 = randomized_select(list_3, 0, len(list_3) - 1, random_3)

    # ordino le liste iniziali
    list_1.sort()
    list_2.sort()
    list_3.sort()

    assert ith_order_statistic_1 == list_1[random_1 - 1]
    assert ith_order_statistic_2 == list_2[random_2 - 1]
    assert ith_order_statistic_3 == list_3[random_3 - 1]


def test_big_random_list():
    """
        Test con liste generate casualmente di 10000 elementi con numeri che vanno da 0 a 100000
    """
    list_1 = random_list_generator(10000, 0, 100000)
    list_2 = random_list_generator(10000, 0, 100000)
    list_3 = random_list_generator(10000, 0, 100000)

    # numeri casuali
    random_1 = randint(0, 10000)
    random_2 = randint(0, 10000)
    random_3 = randint(0, 10000)

    # statistiche d'ordine con i numeri casuali trovati precedentemente
    ith_order_statistic_1 = randomized_select(list_1, 0, len(list_1) - 1, random_1)
    ith_order_statistic_2 = randomized_select(list_2, 0, len(list_2) - 1, random_2)
    ith_order_statistic_3 = randomized_select(list_3, 0, len(list_3) - 1, random_3)

    # ordino le liste iniziali
    list_1.sort()
    list_2.sort()
    list_3.sort()

    assert ith_order_statistic_1 == list_1[random_1 - 1]
    assert ith_order_statistic_2 == list_2[random_2 - 1]
    assert ith_order_statistic_3 == list_3[random_3 - 1]