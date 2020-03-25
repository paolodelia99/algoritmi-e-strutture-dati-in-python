from bitonicSort import bitonic_sort


def test_sample_list():
    sample_list = [10, 30, 11, 20, 4, 330, 21, 110]
    sample_list.sort()
    sorted_sample_list = bitonic_sort(True, sample_list)
    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])