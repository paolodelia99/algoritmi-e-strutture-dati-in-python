class TreeNode:

    def __init__(self, key):
        self.key = key
        self.parent = None  # puntatore al nodo padre
        self.right = None  # puntatore al figlio destro
        self.left = None  # puntatore al figlio sinistro


class BinarySearchTree:
    """
    Classe che rappresenta l'albero binario di ricerca
    """

    def __init__(self, root=None):
        """
            Costruttore dell Albero Binario di Ricerca

            :param root: la radice dell'albero binario, il valore di default è None
        """
        self.root = root

    def insert(self, new_node: TreeNode):
        y, x = None, self.root

        while x is not None:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y

        if y is None:
            self.root = new_node  # l'albero era vuoto
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
