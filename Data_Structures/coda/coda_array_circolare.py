class Coda:
    """ coda con array circolare

    Attributi:
        items (list): array dove verrano memeorizzati gli oggetti (in questo caso i numeri)
        tail (int): puntatore della "tail" della coda
        head (int):puntatore della testa della codae
    """
    def __init__(self, dim):
        self.items = [0] * dim
        self.tail = 0
        self.head = 0

    def is_empty(self):
        return self.tail == 0

    def get_head(self):
        if self.tail == 0:
            raise Exception('La coda è vuota!')
        return self.items[self.head]

    def dequeue(self):
        if self.tail == 0:
            raise Exception('La coda è vuota!')
        t = self.items[self.head]
        self.head = (self.head + 1) % len(self.items)
        self.tail = self.tail - 1
        return t

    def equeue(self, newItem):
        if self.tail == 0:
            raise Exception('La coda è piena!')
        self.items[(self.head + self.tail) % len(self.items)] = newItem
        self.tail = self.tail + 1
