def interpolation_search(A, el):
    """
        Implementazione interpoliation Search

        Parametri
            A lista: array di elementi
            el int: elemento da cercare

        Valore di Ritorno:
            int: indice di el all'interno di A oppure -1 se el non è presente nell'array
    """
    n = len(A)
    low = 0
    high = (n - 1)

    # Siccome l'array è ordinato, l'elemento
    # deve essere nel range definito da low e high
    while low <= high and el >= A[low] and el <= A[high]:
        if low == high:
            if A[low] == el:
                return low
            return -1

        pos = low + int(((float(high - low) /
                          (A[high] - A[low])) * (el - A[low])))

        # Elemento trovato
        if A[pos] == el:
            return pos

        # Se el è maggiore, è nel sottoarray destro
        if A[pos] < el:
            low = pos + 1
        # Se el è minore, è nel sottoarray sinistro
        else:
            high = pos - 1

    return -1
