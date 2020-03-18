from doubleLinkedList import DoubleLinkedList
from node import Node
from nodeFactory import create_node_list_10

dbLinkedList = DoubleLinkedList()


def test_is_empty():
    """
        test metodo is_empty()
    """
    assert dbLinkedList.is_empty() is True


def test_get_head_and_tail():
    """
        test dei metodi get_head e get_tail per dblinkedList vuota
    """
    assert dbLinkedList.get_head() is None
    assert dbLinkedList.get_tail() is None


def test_insert_beginning():
    """
        Test metodo insert beginning
    """
    node_1 = Node(53)
    node_2 = Node(76)
    node_3 = Node(89)
    dbLinkedList.insert_beginning(node_1)
    dbLinkedList.insert_beginning(node_2)
    dbLinkedList.insert_beginning(node_3)
    assert dbLinkedList.get_tail() == node_1
    assert dbLinkedList.get_head() == node_3
    assert dbLinkedList.get_head().get_next() == node_2


def test_insert_after():
    """
        Test del metodo insert_after
    """
    node_1 = Node(53)
    node_2 = Node(45)
    node_3 = Node(6)
    dbLinkedList.insert_beginning(node_1)
    dbLinkedList.insert_after(node_1, node_2)
    dbLinkedList.insert_after(node_2, node_3)
    # verifico che node_1 sia il primo nodo
    assert dbLinkedList.get_head() == node_1
    # verifico che node_2 sia dopo node_1
    assert dbLinkedList.get_head().get_next() == node_2
    # verifico che node_3 sia dopo node_2
    assert dbLinkedList.get_head().get_next().get_next() == node_3


def test_insert_before():
    """
        Test del metodo insert_before
    """
    node_1 = Node(53)
    node_2 = Node(45)
    node_3 = Node(6)
    dbLinkedList.insert_beginning(node_1)
    dbLinkedList.insert_before(node_1, node_2)
    dbLinkedList.insert_before(node_2, node_3)
    # verifico che node_1 sia l'ultimo nodo
    assert dbLinkedList.get_tail() == node_1
    # verifico che node_2 sia prima di node_1
    assert dbLinkedList.get_tail().get_prev() == node_2
    # verifico che node_3 sia prima di node_2
    assert dbLinkedList.get_tail().get_prev().get_prev() == node_3


def test_insert_end():
    """
        Test metodo insert_end
    """
    node_1 = Node(53)
    node_2 = Node(76)
    node_3 = Node(89)
    dbLinkedList.insert_beginning(node_1)
    dbLinkedList.insert_end(node_2)
    dbLinkedList.insert_end(node_3)
    # verifico che node_2 sia il primo nodo
    assert dbLinkedList.get_head() == node_1
    # verifico che node_2 sia il secondo nodo
    assert dbLinkedList.get_head().get_next() == node_2
    # verifico che node_3 sia l'ultimo nodo
    assert dbLinkedList.get_tail() == node_3


def test_remove():
    """
        Test remove()
    """
    node_1 = Node(53)
    node_2 = Node(76)
    node_3 = Node(89)
    dbLinkedList.insert_beginning(node_1)
    dbLinkedList.insert_end(node_2)
    dbLinkedList.insert_end(node_3)
    dbLinkedList.remove(node_1)
    dbLinkedList.remove(node_3)
    assert dbLinkedList.get_head() == node_2
    assert dbLinkedList.get_tail() == node_2


def test_list_search():
    """
        Test ricerca chiave all'interno della lista

        Il metodo create_node_list_10 ritorna una lista di 10 nodi
        e la chiave dell'elemento 4. Dopo aver creato la lista di
        10 nodi effetuo list_search per la chiave ritornata e verifico
        che ritoni in nodo 4
    """
    nodes, to_find_key = create_node_list_10()
    dbLinkedList.insert_beginning(nodes[0])
    for i in range(1, len(nodes)):
        dbLinkedList.insert_end(nodes[i])
    assert dbLinkedList.list_search(to_find_key) == nodes[4]


def test_print_list(capsys):
    """
        Test metodo print_list
    """
    nodes ,key = create_node_list_10()
    #creo la lista di 10 nodi
    dbLinkedList.insert_beginning(nodes[0])
    for i in range(1, len(nodes)):
        dbLinkedList.insert_end(nodes[i])

    dbLinkedList.print_list()
    captured_print = capsys.readouterr()

    for i in range(0,len(nodes)):
        print(nodes[i])
    captured_list = capsys.readouterr()

    assert captured_print == captured_list


def test_print_reverse_list(capsys):
    """
        Test metodo print_list
    """
    nodes ,key = create_node_list_10()
    #creo la lista di 10 nodi
    dbLinkedList.insert_beginning(nodes[0])
    for i in range(1, len(nodes)):
        dbLinkedList.insert_end(nodes[i])

    dbLinkedList.print_reverse_list()
    captured_print = capsys.readouterr()

    for i in range(len(nodes)-1,-1,-1):
        print(nodes[i])
    captured_list = capsys.readouterr()

    assert captured_print == captured_list