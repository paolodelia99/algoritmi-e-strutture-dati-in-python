"""Selection sort
L'algoritmo seleziona di volta in volta il numero minore nella sequenza di partenza e
lo sposta nella sequenza ordinata; di fatto la sequenza viene suddivisa in due parti:
la sottosequenza ordinata, che occupa le prime posizioni dell'array, e la sottosequenza da ordinare,
che costituisce la parte restante dell'array.


Complessità temporale: O(n^2)
"""


# fixme: metodo sbagliato
def selecion_sort(list):
    for j in range(0, len(list) - 1):
        currentMin = j
        for i in range(j + 1, len(list)):
            if list[i] < list[currentMin]:
                currentMin = i
            if currentMin != j:
                list[j], list[currentMin] = list[currentMin], list[j]
