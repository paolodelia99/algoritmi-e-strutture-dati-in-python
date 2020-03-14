from node import Node

class LinkedList:
    """
        Lista singolarmente concatenata

        Attributi:
            head :puntatore al primo elemento della lista
    """
    def __init__(self):
        self.head = Node(None)

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head is None

    def insert(self,node: Node):
        """
            Inserisco elemento all'inizio della lista

            Argomenti:
                node (Node): nuovo nodo da inserire nella lista
        """
        node.set_next(self.head.get_next())
        self.head.set_next(node)

    def insert_after(self, node: Node,new_node: Node):
        """
            Inserice new_node dopo node

            Argomenti:
                node (Node): nodo dopo al quale inserise il nuovo nodo
                new_node (Node): nuovo nodo da inserire
        """
        new_node.set_next(node.get_next())
        node.set_next(new_node)

    def remove_after(self,node: Node):
        """
            Rimuove il nodo successivo al nodo passato per parametro

            Argomenti:
                node (Node): nodo dopo il quale rimuove il nodo successivo
        """
        obsolete_node = node.get_next()
        node.set_next(node.get_next().get_next())
        del obsolete_node

    def remove(self):
        """
            rimuove il primo nodo
        """
        obsolete_node = self.head
        self.head = self.head.get_next
        del obsolete_node

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
