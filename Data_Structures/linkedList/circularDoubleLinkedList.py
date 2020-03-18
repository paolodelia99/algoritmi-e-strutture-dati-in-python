from doubleLinkedList import DoubleLinkedList
from node import Node


class CircularDbLinkedList(DoubleLinkedList):
    """
        Liste doppiamente circolarmente concatenate

        classe figlia di DoubleLinkedList, sovrascrive i metodi:
        insert_after, insert_end, remove,print_list, print_list, print_reverse_list
    """

    def insert_after(self, node: Node, new_node: Node):
        """
            Inserisci new_node dopo node

            Argomenti:
                node (Node):nodo dopo il quale inserire il nuovo nodo
                new_node (Node): nuovo nodo da inserire
        """
        new_node.set_next(node.get_next())
        new_node.set_prev(node)
        # fixme: è sbagliato aggiustalo
        next_node = node.get_next()
        next_node.set_prev(new_node)

        node.set_next(new_node)

    def insert_end(self, node: Node):
        """
            Inserisci il nodo all fine

            Argomenti:
                node (Nodo): nodo da inserire
        """
        if self.tail is None:
            node.set_prev(node)
            node.set_next(node)
        else:
            self.insert_after(self.head,node)
        self.tail = node

    def remove(self, node: Node):
        """
            Rimuovi nodo

            Argomenti:
                node (Node): nodo da rimuovere
        """
        if node.get_next() is node:
            self.tail = None
        else:
            node.get_next().set_prev(node.get_prev())
            node.get_prev().set_next(node.get_next())
            if node is self.tail:
                self.tail = node.get_prev()
        del node

    def print_list(self):
        """
            Stampo nell'ordine la lista
        """
        node = self.head
        print(node)
        node = node.get_next()

        while node is not self.head:
            print(node)
            node = node.get_next()

    def print_reverse_list(self):
        """
            Stampo la lista nell'ordine inverso
        """
        node = self.tail
        print(node)
        node = node.get_prev()

        while node is not self.tail:
            print(node)
            node = node.get_prev()
