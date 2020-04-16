from scambleSearch import scramble_search
from randomListGenerator import small_random_list_generator
import random


def test_sample_list():
    # Test con la sample_list
    sample_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert 6 == scramble_search(sample_list, 8)


def test_random_lists():
    # Random Tests
    list1 = small_random_list_generator()
    list2 = small_random_list_generator()
    list3 = small_random_list_generator()

    # Selgo un elemento a caso per ciascuna lista
    element1 = list1[random.randint(0, len(list1))]
    element2 = list2[random.randint(0, len(list2))]
    element3 = list3[random.randint(0, len(list3))]
    assert list1.index(element1) == scramble_search(list1, element1)
    assert list2.index(element2) == scramble_search(list2, element2)
    assert list3.index(element3) == scramble_search(list3, element3)
