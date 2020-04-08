from countingSort import counting_sort


def radix_sort(A):
    """
        Implementazione di radix sort utilizzando counting sort come array di oridnamento stabile

        Argomenti:
            A (list): lista di interi da ordinare
    """
    max1 = max(A)

    exp = 1
    while max1 / exp > 0:
        counting_sort(A, [0 * len(A)], exp)
        exp *= 10
