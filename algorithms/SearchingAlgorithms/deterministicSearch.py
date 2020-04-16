def linear_search(A, element):
    """
        Implementazione riceca sequenziale

        parametri:
            A list: lista
            element int: elemento da cercare

        valore di ritorno:
            int: indice dell'elemente all'interno della lista altrmenti -1 se l'elemento non è presente
    """
    for i in range(0, len(A)):
        if A[i] == element:
            return i

    return -1
