from countingSort import counting_sort


# Sample test

def test_sample_list():
    sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    order_list = [0] * len(sample_list)
    counting_sort(sorted_sample_list, order_list, max(sample_list))
    # ordino sample_list con il metodo sort()
    sample_list.sort()
    assert all([a == b for a, b in zip(sample_list, order_list)])
