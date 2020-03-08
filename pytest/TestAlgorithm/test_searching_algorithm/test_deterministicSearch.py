from deterministicSearch import linear_search
from randomListGenerator import small_random_list_generator
import random

# Test con la sample_list
sample_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]


def test_sample_list():
    assert 6 == linear_search(sample_list, 8)


# Random Tests
list1 = small_random_list_generator()
list2 = small_random_list_generator()
list3 = small_random_list_generator()

# Selgo un elemento a caso per ciascuna lista
element1 = list1[random.randint(0, len(list1))]
element2 = list2[random.randint(0, len(list2))]
element3 = list3[random.randint(0, len(list3))]


def test_random_lists():
    assert list1.index(element1) == linear_search(list1, element1)
    assert list2.index(element2) == linear_search(list2, element2)
    assert list3.index(element3) == linear_search(list3, element3)
