# Test binary Search
from binarySearch import binary_search
import random

# Test con la sample_list
sample_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]


def test_sample_list():
    assert True == binary_search(sample_list, 8)


# Random Tests
list1 = []
list2 = []
list3 = []

for i in range(random.randint(10, 22)):
    list1.append(random.randint(1, 101))

for i in range(random.randint(10, 22)):
    list2.append(random.randint(1, 101))

for i in range(random.randint(10, 22)):
    list3.append(random.randint(1, 101))

# ordino le liste ( dato altrimenti la binary search presuppone che la lista sia ordinata)
list1.sort()
list2.sort()
list3.sort()

# Seglo un elemento a caso di ciascuna lista
element1 = list1[random.randint(0, len(list1))]
element2 = list2[random.randint(0, len(list2))]
element3 = list3[random.randint(0, len(list3))]


def test_random_lists():
    assert True == binary_search(list1, element1)
    assert True == binary_search(list2, element2)
    assert True == binary_search(list3, element3)
