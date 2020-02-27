# fixme: metodo sbagliato
def selecion_sort(list_):
    """
    Implementazione di selection sort

    Parametri
        list_ (list): lista di numeri interi da ordinare
    """
    for j in range(0, len(list_) - 1):
        currentMin = j
        for i in range(j + 1, len(list_)):
            if list_[i] < list_[currentMin]:
                currentMin = i
            if currentMin != j:
                list_[j], list_[currentMin] = list_[currentMin], list_[j]
