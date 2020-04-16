def insertion_sort(A):
    """
        Insertion sort

        Argomenti:
            A (list): array da ordinare
    """
    for j in range(1, len(A)):

        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key
