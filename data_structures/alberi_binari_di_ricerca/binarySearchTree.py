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


    def inorder(self, node: TreeNode):
        """Visita dell'albero in ordine con una procedura ricorsiva

        Arguments:
            node {TreeNode} -- Il nodo radice da visitare
        """
        if node is None:
            inorder(x.left)
            print(x)
            inorder(x.right)


    def preoder(self, x: TreeNode):
        """Visita dell'abero in preordine con procedura ricorsiva

        Arguments:
            x {TreeNode} -- Il nodo radice da visitare
        """
        if x is not None: 
            print(x.key)
            preorder(x.left)
            preorder(x.right)
    
    def postorder(self, x:TreeNode):
        """Visita dell'albero in postordine con procedura ricorsiva

        Arguments:
            x {TreeNode} -- Il nodo radice da visitare
        """
        if x is not None:
            postorder(x.left)
            postorder(x.right)
            print(x.key)

    def inorder_it(self):
        """Visita dell'albero in ordine con una procedura iterativa
        """
        if self.root == None:
        return

        stack = []
        curr_node = self.root
        
        while stack or curr_node is not None:
        if curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.left
        else:
            curr_node = stack[-1]
            stack.pop()
            print(curr_node.key)
            curr_node = curr_node.right

    def insert(self, new_node: TreeNode):
        """Inserimento di un nodo all'interno dell'albero binario di ricerca

        Arguments:
            new_node {TreeNode} -- nodo da inserite nell'albero
        """
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

    
    def search(self,x:TreeNode, k):
        """Ricerca di una chiave all'interno del albero attraverso una procedura ricorsiva

        Arguments:
            x {TreeNode} -- Il nodo con cui confontare la chiave da cercare
            k {[type]} -- la chiave da ricercare

        Returns:
            TreeNode -- Il nodo contenente la chiave ricercata oppure il Nodo null
        """
        if x is None or k == x.key:
            return x
        
        if k < x.key:
            return search(x.left, k)
        else:
            return search(x.rigth, k)

    def minimum(self, x):
        """Ritorna il nodo che possiede la chiave di valore minimo

        Arguments:
            x {TreeNode} -- nodo dell'abero

        Returns:
            TreeNode -- nodo dell'abero con chiave minima
        """
        while x.left is not None:
            minimum(x.left)
        return x

    def maximum(self, x:TreeNode) -> TreeNode:
        """Ritorna il nodo che possiede la chiave di valore massimo

        Arguments:
            x {TreeNode} -- nodo dell'albero

        Returns:
            TreeNode -- nodo dell'albero con chiave massima
        """
        while x.right is not None:
            maximum(x.right)
        return x


    def successor(self, x:TreeNode) -> TreeNode:
        """Ritorna il nodo successore del nodo dell'albero dato come input

        Arguments:
            x {TreeNode} -- nodo cui bisogna trovare il successore

        Returns:
            TreeNode -- Successore del nodo dato come input
        """
        if x.right is not None:
            return self.minimum(x.right)
        
        y = x.parent

        while y is not None and x == y.right:
            x = y
            y = x.parent
        
        return y

    def predecessor(self, x:TreeNode) -> TreeNode:
        """Ritorna il nodo predecessore del nodo dell'albero dato come input

        Arguments:
            x {TreeNode} -- nodo cui bisogna trovare il predecessore

        Returns:
            TreeNode -- Predecessore del nodo dato come input
        """
        if x.left is not None:
            return self.maximum(x.left)
        
        y = x.parent

        while y is not None and x == y.left:
            x = y
            y = x.parent
        
        return y


        def transplant(self, u:TreeNode, v:TreeNode):
            """Sostituisce un sottoalbero, come figlio di suo padre, con un altro sottoalbero

            Arguments:
                u {TreeNode} -- radice del sottoalbero da sostituire
                v {TreeNode} -- radice del sottoalbero da inserire
            """
            if u.parent is None: # l'albero è vuoto
                self.root = v
            elif u == u.parent.left: # u è figlio sinistro 
                u.parent.left = v
            else: # u è figlio destro
                u.parent.right = v

            if v is not None: # aggiornamento di v.parent se v non è None
                v.parent = u .parent


        def delete(self, z:TreeNode):
            """Rimozione del nodo dato come input dall'albero

            Arguments:
                z {TreeNode} -- nodo dell'albero da rimuovere
            """
            if z.left is None:
                self.transplant(z, z.right)
            elif z.right is None:
                self.transplant(z, z.left)
            else:
                y = minimum(z.right)

                if y.parent != z:
                    self.transplant(y, t.right)
                    y.right = z.right
                    y.right.parent = y
                
                self.transplant(z,y)
                y.left = z.left
                y.left.parent = y
