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
    step = math.floor(math.sqrt(len(n)))

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while A[int(min(step, n) - 1)] < el:
        prev = step
        step = math.floor(math.sqrt(n))
        if prev >= n:
            return -1

    # Doing a linear search for x in
    # block beginning with prev
    while A[int(prev)] < el:
        prev += 1

        if prev == min(step,n):
            return -1

    # If element is found
    if A[int(prev)] == el:
        return prev

    return -1
