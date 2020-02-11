class Heap:
    def __init__(self, list_):
        self.container = list_
        self.size = len(self.container)

    def get_parent(self, index):
        return (index - 1) // 2

    def get_left_child(self, index):
        return 2 * index + 1

    def get_right_child(self, index):
        return (2 * index) + 2

    def get_size(self):
        return self.size

    def get_item(self, index):
        return self.container[index]

    def get_max(self):
        if self.size == 0:
            return None
        return self.container[0]

    def extract_max(self):
        if self.size == 0:
            return None
        largest = self.get_max()
        self.container[0] = self.container[-1]
        del self.container[-1]
        self.max_heapify(0)
        return largest

    def max_heapify(self, index):
        l = self.get_left_child(index)
        r = self.get_right_child(index)

        if l <= self.size - 1 and self.container[l] > self.container[index]:
            largest = l
        else:
            largest = index

        if r <= self.size - 1 and self.container[r] > self.container[largest]:
            largest = r

        if largest != index:
            self.swap(largest, index)
            self.max_heapify(largest)

    def build_max_heap(self):
        self.size = len(self.container)
        for i in range((len(self.container) // 2), -1, -1):
            self.max_heapify(i)

    def swap(self, i, j):
        self.container[i], self.container[j] = self.container[j], self.container[i]

    def insert(self, key):
        index = self.size
        self.container.append(key)

        while index != 0:
            p = self.get_parent(index)
            if self.get_item(p) < self.get_item(index):
                self.swap(p, index)
            index = p

    def min_heapify(self, index):
        l = self.get_left_child(index)
        r = self.get_right_child(index)
        if l <= self.size and self.container[l] < self.container[index]:
            minimun = l
        else:
            minimun = index

        if r <= self.size and self.container[r] < self.container[index]:
            minimun = r

        if minimun != index:
            self.swap(minimun, index)
            self.min_heapify(minimun)

    def build_min_heap(self):
        self.size = len(self.container)
        for i in range((len(self.container) // 2), 0):
            self.min_heapify(self.container, i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self.container) - 1, -1, -1):
            self.swap(0, i)
            self.size = self.size - 1
            self.max_heapify(0)
