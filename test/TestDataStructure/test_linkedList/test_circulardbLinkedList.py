from circularDoubleLinkedList import CircularDbLinkedList
from node import Node
from nodeFactory import create_node_list_10

cirDbLinkedList = CircularDbLinkedList()


def test_is_empty():
    """
        test metodo is_empty()
    """
    assert cirDbLinkedList.is_empty() is True


def test_get_head_and_tail():
    """
        test dei metodi get_head e get_tail per dblinkedList vuota
    """
    assert cirDbLinkedList.get_head() is None
    assert cirDbLinkedList.get_tail() is None


def test_insert_beginning():
    """
        Test metodo insert beginning
    """
    node_1 = Node(53)
    node_2 = Node(76)
    node_3 = Node(89)
    cirDbLinkedList.insert_beginning(node_1)
    cirDbLinkedList.insert_beginning(node_2)
    cirDbLinkedList.insert_beginning(node_3)
    assert cirDbLinkedList.get_tail() == node_1
    assert cirDbLinkedList.get_head() == node_3
    assert cirDbLinkedList.get_head().get_next() == node_2


def test_insert_after():
    """
        Test del metodo insert_after
    """
    node_1 = Node(53)
    node_2 = Node(45)
    node_3 = Node(6)
    cirDbLinkedList.insert_beginning(node_1)
    cirDbLinkedList.insert_after(node_1, node_2)
    cirDbLinkedList.insert_after(node_2, node_3)
    # verifico che node_1 sia il primo nodo
    assert cirDbLinkedList.get_head() == node_1
    # verifico che node_2 sia dopo node_1
    assert cirDbLinkedList.get_head().get_next() == node_2
    # verifico che node_3 sia dopo node_2
    assert cirDbLinkedList.get_tail().get_prev() == node_3
