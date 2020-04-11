from quickSort import randomize_partition


def randomized_select(A: list, p: int, r: int, i: int):
    """
        Implementazione ricorisiva dell'algoritmo randomizeSelect che ritorna
        l'i-esima statistica d'ordine dell'array di input

        Parametri:
            A (list): lista di elementi
            p (int): indice di inizio dell'array
            r (int): indice di fine array
            i (int): i-esima statistica d'ordine rihciesta

        Valore di ritorno:
            i-esima statistica dell'array dato in input
    """
    if p == r:
        return A[p]

    q = randomize_partition(A, p, r)
    k = q - p + 1

    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)
