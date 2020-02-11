"""Bubble Sort

Bubble sort è un semplice algoritmo di ordinamento di una lista di dati.
Ogni coppia di elementi adiacenti viene comparata e invertita di posizione se sono nell'ordine sbagliato.
L'algoritmo continua nuovamente a ri-eseguire questi passaggi per tutta la lista finché
non vengono più eseguiti scambi, situazione che indica che la lista è ordinata

Tempo di esecuzione: O(n^2)
"""


def bubble_sort(list):
    """Bubble sort
    
    Argomenti:
        list {[int]} -- lista di numeri non ordinati
    """
    for i in range(0, len(list) - 1):
        for j in range(len(list) - 1, i, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]