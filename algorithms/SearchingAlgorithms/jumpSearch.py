import math


def jump_search(A, el):
    """
        Implementazione di jump search

        Parametri
            A lista: lista di elementi
            el int: numero da trovare

        Valore di ritorno
            int: indice dell'elemento se presente altrimenti -1
    """
    n = len(A)
    # Finding block size to be jumped
    step = math.sqrt(n)

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while A[int(min(step, n) - 1)] < el:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Doing a linear search for x in
    # block beginning with prev.
    while A[int(prev)] < el:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1

    # If element is found
    if A[int(prev)] == el:
        return int(prev)

    return -1