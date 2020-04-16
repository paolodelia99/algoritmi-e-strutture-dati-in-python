from deterministicSearch import linear_search
from randomizeInPlace import randomize_in_place


# fixme da rifare
def scramble_search(A, el):
    """
        Implementazione di Scamble  Search

        Argomenti:
            A list: array di elementi
            el int: numero da trovare

        Valore di Ritorno:
            int: indice dell'elemento da torvare
    """
    A = randomize_in_place(A)
    if linear_search(A, el) != -1:
        return linear_search(A, el)
    else:
        return -1
