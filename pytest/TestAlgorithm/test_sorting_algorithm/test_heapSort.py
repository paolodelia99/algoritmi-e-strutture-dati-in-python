# Test heap sort
from heap import Heap
import random

sample_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
sample_heap = Heap(sample_list)  # inizializzo l'heap
sample_heap.heap_sort()
sample_list.sort()


# Testo heapsort per la sample_list
def test_sample_list():
    assert all([a == b for a, b in zip(sample_list, sample_heap.container)])

# test liste create casualmente
list1 = []
list2 = []
list3 = []

for i in range(random.randint(10, 22)):
    list1.append(random.randint(1, 101))

for i in range(random.randint(10, 22)):
    list2.append(random.randint(1, 101))

for i in range(random.randint(10, 22)):
    list3.append(random.randint(1, 101))


# copio le liste precedentemente create nell corrispettive sorted_list e creo i corrispettvi Heap
sorted_list1 = list1.copy()
sorted_list2 = list2.copy()
sorted_list3 = list3.copy()
heap_1 = Heap(sorted_list1)
heap_2 = Heap(sorted_list2)
heap_3 = Heap(sorted_list3)
# le ordino con insetion_sort
heap_1.heap_sort()
heap_2.heap_sort()
heap_3.heap_sort()
# ordino le liste randomiche precedentemente create con il metodo sort()
list1.sort()
list2.sort()
list3.sort()


def test_random_list():
    assert all([a == b for a, b in zip(list1, heap_1.container)])
    assert all([a == b for a, b in zip(list2, heap_2.container)])
    assert all([a == b for a, b in zip(list3, heap_3.container)])
