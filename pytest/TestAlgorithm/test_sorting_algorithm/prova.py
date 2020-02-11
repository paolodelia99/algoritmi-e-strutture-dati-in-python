from heap import Heap

sample_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heap_1 = Heap(sample_list)  # inizializzo l'heap
print(heap_1.container)
heap_1.heap_sort()
print(heap_1.container)
sample_list.sort()

print(all([a == b for a, b in zip(sample_list, heap_1.container)]))