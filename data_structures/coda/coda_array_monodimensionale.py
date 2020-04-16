"""
Implementazione della coda utilizzando l'oggetto
deque dalla classe collections
"""
from collections import deque

# fixme: da rifare


class Coda:
    def __init__(self, list_):
        self.items = deque(list_)
        self.head = 0
        self.tail = len(self.items)

    def is_empty(self):
        return self.items.maxlen == 0

    def enqueue(self, x):
        # la funzione append aggiunge un elemento alla sinistra della coda
        self.items.append(x)
        if self.tail == len(self.items):
            self.tail = 1
        else:
            self.tail = self.tail + 1

    def dequeue(self):
        # la funzione popleft rimuove l'elemento più a sinistra della coda (cioè il primo)
        self.items.popleft()
        if self.head == len(self.items):
            self.head = 1
        else:
            self.head = self.head + 1
