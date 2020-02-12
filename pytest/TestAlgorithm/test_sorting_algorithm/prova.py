from quickSort import quicksort, randomize_quicksort

sample_list = [5, 2, 4, 7, 1, 3, 2, 6]
# copio sample list in sorted_sample_list
sorted_sample_list = sample_list.copy()
# la ordino
quicksort(sorted_sample_list, 0, len(sorted_sample_list)-1)
# randomize_quicksort(sorted_sample_list, 0, len(sorted_sample_list)-1)
# ordino sample_list con il metodo sort()
sample_list.sort()
print(f'sorted sample: {sorted_sample_list}')
print(f'final sample list {sample_list}')