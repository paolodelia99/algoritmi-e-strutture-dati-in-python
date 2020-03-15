from linkedList import LinkedList
from node import Node

node_1 = Node(25)
node_2 = Node(45)
node_3 = Node(1)
linked_list = LinkedList()

print(linked_list.is_empty())

linked_list.insert(node_1)
print(linked_list.get_head().get_next().get_key())

linked_list.insert(node_2)
linked_list.insert(node_3)

linked_list.print_list()
