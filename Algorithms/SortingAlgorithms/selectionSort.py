# fixme: metodo sbagliato
def selecion_sort(list_):
    """Implementazione di selection sort

    Parametri
        list_ (list): lista di numeri interi da ordinare
    """
    for j in range(0, len(list_) - 1):
        current_min = j
        for i in range(j + 1, len(list_)):
            if list_[i] < list_[current_min]:
                current_min = i
            if current_min != j:
                # scambio il numero al l'indice j con il numero all'indice current_min
                list_[j], list_[current_min] = list_[current_min], list_[j]
