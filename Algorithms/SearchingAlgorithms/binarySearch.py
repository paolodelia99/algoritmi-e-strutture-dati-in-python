"""Binary Search 

implementazione delle versione ricorsiva e iterativa della binary search

"""


def binary_search(list_, element):
    """ ricerca binaria versione ricorsiva

           Parametri:
           list_ (list): lista di numeri interi
           element (int): elemento da trovare

           Valore di Ritorno:
           int: indice dell'elemento all'interno dell'array, altrimenti se non è presente ritorna -1
       """
    mid = len(list_) // 2
    if len(list_) == 1 and element != list_[mid]:
        return -1
    elif element == list_[mid]:
        return mid
    elif element < list_[mid]:
        return binary_search(list_[0:mid], element)
    else:
        return binary_search(list_[mid:len(list_)], element)


def binary_search_iterative(list_, p, r, element):
    """ ricerca binaria versione iterativa

        Parametri:
        list_ (list): lista di numeri interi
        p (int): indice di inzio dell'array
        r(int): indice di fine dell'array
        element (int): elemento da trovare

        Valore di Ritorno:
        int: indice dell'elemento all'interno dell'array, altrimenti se non è presente ritorna -1
    """
    # Controllo che l'elemento non sia fuori dal range della lista
    if element < list_[p] or element > list_[r]:
        return -1

    while p <= r:
        q = (p + r) // 2 # trovo l'elemento centrale
        if list_[q] == element:
            return q
        if list_[q] > element:
            r = q - 1
        else:
            p = q + 1

    return -1
