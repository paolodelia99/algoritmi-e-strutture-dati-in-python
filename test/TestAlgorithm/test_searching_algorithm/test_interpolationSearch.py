from interpolationSearch import interpolation_search
import random
from randomListGenerator import small_random_list_generator


def test_sample_list():
    # Test con la sample_list
    sample_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    assert 6 == interpolation_search(sample_list, 8)


def test_random_lists():
    # Random Tests
    list1 = small_random_list_generator()
    list2 = small_random_list_generator()
    list3 = small_random_list_generator()

    # ordino le liste dato che l'algoritmo presuppone che le liste siano ordinate
    list1.sort()
    list2.sort()
    list3.sort()

    # Selgo un elemento a caso per ciascuna lista
    element1 = list1[random.randint(0, len(list1) - 1)]
    element2 = list2[random.randint(0, len(list2) - 1)]
    element3 = list3[random.randint(0, len(list3) - 1)]
    assert list1.index(element1) == interpolation_search(list1, element1)
    assert list2.index(element2) == interpolation_search(list2, element2)
    assert list3.index(element3) == interpolation_search(list3, element3)
