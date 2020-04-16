from binarySearch import binary_search
from randomListGenerator import small_random_list_generator
import random


def test_sample_list():
    # Test con la sample_list
    sample_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert True == binary_search(sample_list, 8)


def test_random_lists():
    # Random Tests
    list1 = small_random_list_generator()
    list2 = small_random_list_generator()
    list3 = small_random_list_generator()

    # ordino le liste ( dato altrimenti la binary search presuppone che la lista sia ordinata)
    list1.sort()
    list2.sort()
    list3.sort()

    # Seglo un elemento a caso di ciascuna lista
    element1 = list1[random.randint(0, len(list1))]
    element2 = list2[random.randint(0, len(list2))]
    element3 = list3[random.randint(0, len(list3))]
    assert True == binary_search(list1, element1)
    assert True == binary_search(list2, element2)
    assert True == binary_search(list3, element3)
