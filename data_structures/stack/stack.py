class Stack:
    """Implementazione dello stack basato su un vettore

    Attributi:
        items (list): contenitore dello stack
        m (int): dimensione massima dello stack
        top (int): indice (o puntatore) dell'elemento inserito più recentemente
    """

    def __init__(self, dim):
        self.items = [] * dim
        self.m = dim  # dimensione massima array
        self.top = 0  # ountatore al ultimo elemento inserito nell stack

    # Ritorna True se lo stack è vuoto
    def is_empty(self):
        return self.top == 0

    # inserisce un elemento nello stack
    def push(self, item):
        if self.top == self.m:
            raise Exception('Lo stack è pieno!')
        self.items.append(item)

    # rimuove l'ultimo elemento dello stack
    def pop(self):
        if self.top == 0:
            raise Exception('Lo stack è vuoto!')
        return self.items.pop()

    # restituisce l'ultimo elemento dello stack
    def peek(self):
        if self.top == 0:
            raise Exception("Lo stack è vuoto!")
        return self.items[self.top]

    # ritorna la dimensione dello stack
    def size(self):
        return len(self.items)

    # ritorna tutto lo stack
    def show(self):
        return self.items
