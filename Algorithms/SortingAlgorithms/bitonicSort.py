def bitonic_sort(up: bool, x: list):
    """Bitonic Sort

        Argomenti:
            up (bool): se è vero si ordine crescente, altimenti decrescente
            x (list): lista di numeri interi

        Valore di ritorno:
            lista di numeri interi ordinati
    """
    if len(x) <= 1:
        return x
    else:
        first = bitonic_sort(True, x[:len(x) // 2])
        second = bitonic_sort(False, x[len(x) // 2:])
        return bitonic_merge(up, first + second)


def bitonic_merge(up: bool, x):
    """
        todo
    """
    if len(x) == 1:
        return x
    else:
        bitonic_compare(up, x)
        first = bitonic_merge(up, x[:len(x) // 2])
        second = bitonic_merge(up, x[len(x) // 2:])
        return first + second


def bitonic_compare(up: bool, x):
    """
        todo
    """
    dist = len(x) // 2
    for i in range(dist):
        if (x[i] > x[i + dist]) == up:
            x[i], x[i + dist] = x[i + dist], x[i]  # Swap
