import mainPackage.SortingAlgorithms.insertionSort

sample_list = [3,5,1,9,8,2]

def sample_test():
    assert sample_list.sort() == insertionSort.insertion_sort(sample_list)