# Test Quick sort
from quickSort import quicksort, randomize_quicksort

# test quicksort
sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
# copio sample list in sorted_sample_list
sorted_sample_list = sample_list.copy()
# la ordino
quicksort(sorted_sample_list, 0, len(sorted_sample_list) - 1)
# ordino sample_list con il metodo sort()
sample_list.sort()


def test_sample_list():
    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])


# test random_quicksort
sample_list_1 = [5, 2, 4, 7, 1, 3, 2, 6]
# copio sample list in sorted_sample_list
sorted_sample_list_1 = sample_list.copy()
# la ordino
randomize_quicksort(sorted_sample_list_1, 0, len(sorted_sample_list_1) - 1)
# ordino sample_list con il metodo sort()
sample_list_1.sort()


def test_sample_list_random_algo():
    assert all([a == b for a, b in zip(sample_list_1, sorted_sample_list_1)])
