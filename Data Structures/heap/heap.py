class Heap:
    def __init__(self):
        self.container = []
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

    def max_heapify(self, i):
        l = self.get_left_child(i)
        r = self.get_right_child(i)
        if l <= self.size - 1 and self.get_item(l) > self.get_item(i):
            largest = l
        else:
            largest = i
        if r <= self.size - 1 and self.get_item(r) > self.get_item(largest):
            largest = r
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)

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

    # fixme: min heap stuff