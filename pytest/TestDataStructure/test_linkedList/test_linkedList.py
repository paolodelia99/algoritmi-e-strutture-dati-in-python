import sys
from linkedList import LinkedList
from node import Node

linked_list_sample = LinkedList()

# Test metodo is empty
def test_is_empty():
    assert linked_list_sample.is_empty() is True

# Test metodo get_head
def test_get_head():
    assert linked_list_sample.get_head() is None


linked_list_1 = LinkedList()
node_1 = Node(25)
linked_list_1.insert(node_1)


#test metodo insert
def test_insert():
    assert linked_list_1.get_head().get_key() == node_1.get_key()


linked_list = LinkedList()
linked_list.insert(node_1)
node_2 = Node(45)
node_3 = Node(1)
linked_list.insert_after(node_1, node_2)


# Test metodo insert_after
def test_insert_after():
    assert linked_list.get_head().get_next() == node_2


linked_list.insert_after(node_2, node_3)


# Test metodo list_search
def test_list_search():
    assert linked_list.list_search(25) == node_1
    assert linked_list.list_search(45) == node_2
    assert linked_list.list_search(1) == node_3


# Test print_list
def test_print_list(capsys):
    linked_list.print_list()
    captured = capsys.readouterr()
    assert captured.out == "key: 25\nkey: 45\nkey: 1\n"


# Test remove()
def test_remove():
    linked_list.remove()
    assert linked_list.get_head() == node_2


# Test remove after
def test_remove_after():
    linked_list.remove_after(node_1)
    assert linked_list.get_head().get_next() == node_3
