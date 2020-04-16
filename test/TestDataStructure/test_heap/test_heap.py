from heap import Heap

# default list
list_ = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

test_heap = Heap(list_)


# Testo il metodo di get_right_child()
def test_get_right_child():
    assert 3 == list_[test_heap.get_right_child(0)]
    assert 10 == list_[test_heap.get_right_child(2)]
    assert 16 == list_[test_heap.get_right_child(1)]
    assert 8 == list_[test_heap.get_right_child(3)]


# Testo il metodo get_left_child()
def test_get_left_child():
    assert 1 == list_[test_heap.get_left_child(0)]
    assert 2 == list_[test_heap.get_left_child(1)]
    assert 9 == list_[test_heap.get_left_child(2)]
    assert 14 == list_[test_heap.get_left_child(3)]
    assert 7 == list_[test_heap.get_left_child(4)]


# Testo il metodo get_parent()
def test_get_parent():
    assert 4 == list_[test_heap.get_parent(1)]
    assert 4 == list_[test_heap.get_parent(2)]
    assert 1 == list_[test_heap.get_parent(3)]
    assert 1 == list_[test_heap.get_parent(4)]
    assert 3 == list_[test_heap.get_parent(5)]
    assert 3 == list_[test_heap.get_parent(6)]
    assert 2 == list_[test_heap.get_parent(7)]
    assert 2 == list_[test_heap.get_parent(8)]
    assert 16 == list_[test_heap.get_parent(9)]


# Testo il metodo get_size()
def test_get_size():
    assert 10 == test_heap.get_size()


# Testo il get_item()
def test_get_item():
    assert 4 == test_heap.get_item(0)


list_1 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
test_heap_1 = Heap(list_1)
test_heap_1.max_heapify(1)


# testo il max_heapify su list_1
def test_max_heapify():
    assert all([a == b for a, b in zip([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], test_heap_1.container)])


list_2 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
test_heap_2 = Heap(list_2)
test_heap_2.build_max_heap()


# testo il build_max_heap su list_2
def test_build_max_heap():
    assert all([a == b for a, b in zip([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], test_heap_1.container)])