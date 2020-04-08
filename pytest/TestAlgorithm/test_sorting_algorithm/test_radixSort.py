from radixSort import radix_sort
from randomListGenerator import small_random_list_generator, big_random_list_generator


# Sample test
# fixme: da fare è sbagliato
def test_sample_list():
    sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
    # copio sample list in sorted_sample_list
    sorted_sample_list = sample_list.copy()
    # la ordino
    radix_sort(sorted_sample_list)
    # ordino sample_list con il metodo sort()
    sample_list.sort()
    assert all([a == b for a, b in zip(sample_list, sorted_sample_list)])