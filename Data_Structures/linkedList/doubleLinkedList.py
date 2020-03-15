from node import Node


class DoubleLinkedList:
    """
        Lista doppiamente concatenata

        Attributi:
            head : puntatore al primo elemento della lista
            tail: puntatore al secondo elemento della lista
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def insert(self, node: Node):
        """
            Inserisco l'elemento all'inizio della lista

            Argomenti:
                node (Node): nuovo nodo da inserire
        """
        node.set_next(self.head.get_next() if self.head is not None else None)
        if self.head is not None:
            self.head.set_prev(node)
        self.head = node
        node.set_prev(None)

    def insert_after(self, node: Node, new_node: Node):
        """
            Inserice new_node dopo node

            Argomenti:
                node (Node): nodo dopo al quale inserise il nuovo nodo
                new_node (Node): nuovo nodo da inserire
        """
        new_node.set_next(node.get_next())
        new_node.set_prev(node)

        # Se node è l'ultimo elemento allora poni tail = new_node
        if node.get_next() is None:
            self.tail = new_node
        else:
            node.get_next().set_prev(new_node)

        node.set_next(new_node)

    def insert_before(self, node: Node, new_node: Node):
        """
            Inserisce new_node prima di node

            Argomenti:
                    node (Node): nodo dopo al quale inserise il nuovo nodo
                    new_node (Node): nuovo nodo da inserire
        """
        new_node.set_next(node)
        new_node.set_prev(node.get_prev())

        if node.get_prev() is None:
            self.head = new_node
        else:
            node.get_prev().set_next(new_node)

        node.set_prev(new_node)

    def insert_beginning(self, node: Node):
        """
            Inserisci node all'inizio della lista

            Argomenti:
                node (Node): nuovo nodo da inserire all'inizio della lista
        """
        if self.head is None:
            self.head = node
            self.tail = node
            node.set_prev(None)
            node.set_next(None)
        else:
            self.insert_before(self.head, node)

    def insert_end(self, node: Node):
        """
            Inserisce il nodo all fine della lista

            Argomenti:
                node (Node): nuovo nodo da inserire alla fine della lista
        """
        if self.tail is None:
            self.insert_beginning(node)
        else:
            self.insert_after(self.head, node)

    def remove(self, node: Node):
        """
            Rimuovi il nodo node dalla lista

            Argomenti:
                node (Node): nodo da rimuovere
        """
        if node.get_prev() is None:
            self.head = node.get_next()
        else:
            node.get_prev().set_next(node.get_next())

        if node.get_next() is None:
            self.tail = node.get_prev()
        else:
            node.get_next().set_prev(node.get_prev())

        del node

    def list_search(self, key):
        """
                  Cerco all'interno della lista il nodo con chiave = key

                  Argomenti:
                      key : chiave da trovare all'interno della lista

                  Valore di ritorno
                      Node: nodo con chiave = key altrimenti None
              """
        node = self.head

        while node is not None and node.key != key:
            node = node.get_next()

        return node

    def print_list(self):
        """
            Stampa la lista in ordine
        """
        node = self.head

        while node is not None:
            print(node)
            node = node.get_next()

    def print_reverse_list(self):
        """
            Stampa la lista in ordine inverso
        """
        node = self.tail

        while node is not None:
            print(node)
            node = node.get_prev()
