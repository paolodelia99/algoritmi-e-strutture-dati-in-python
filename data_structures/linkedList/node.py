class Node:
    """
        Classe Nodo di un lista

        Attributi:
            prev (int): puntatore all'elemento successivo della lista
            next (int): puntatore all'elemento precedente della lista
            key (oggetto): oggetto/numero memorizzato nella lista
    """

    def __init__(self, key, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.key = key

    def get_key(self):
        return self.key

    def set_prev(self, new_prev):
        self.prev = new_prev

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def __str__(self):
        return "key: " + str(self.key)+""
