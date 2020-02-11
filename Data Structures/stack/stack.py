class Stack:
    # "Costruttuore dello stack"
    def __init__(self):
        self.container = []

    # Ritorna True se lo stack è vuoto
    def is_empty(self):
        return self.size() == 0

    # inserisce un elemento nello stack
    def push(self, item):
        self.container.append(item)

    # rimuove l'ultimo elemento dello stack
    def pop(self):
        return self.container.pop()

    # restituisce l'ultimo elemento dello stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack empty!")
        return self.container[-1]

    # ritorna la dimensione dello stack
    def size(self):
        return len(self.container)

    # ritorna tutto lo stack
    def show(self):
        return self.container