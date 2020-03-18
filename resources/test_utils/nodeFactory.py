from node import Node
from random import randint


def create_node_list_10():
    """
        Metodo che ritorna una lista di 10 nodi e la chiave dell'elemento centrale
    """
    nodes = []
    to_find_key = None
    for i in range(0, 10):
        key = randint(1, 101)
        node = Node(key)
        if i == 4:
            to_find_key = key
        nodes.append(node)

    return nodes, to_find_key
