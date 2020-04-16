""" Quicksort

Implementazione degli algoritmi di quicksort e random_quicksort, delle corrispettive procedure

quicksort
complessità temporale: caso peggiore O(n^2)
                       caso medio Θ(n ln(n))

random_quicksort: tempo di esecuzione atteso O(n ln(n))
"""
from random import randint


def quicksort(A, p, r):
    """implementazione ricorsiva di quicksort

        Parametri:
        A (list): lista di numeri interi
        p (int): indice di inzio dell'array(o sottoarray)
        r(int): indice di fine dell'array(o sottoarray)
    """
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    """procedura partition

         Parametri:
            A (int): lista di numeri interi
            p (int): indice di inzio dell'array(o sottoarray)
            r(int): indice di fine dell'array(o sottoarray)

        Valore di Ritorno:
        int: indice del pivot
    """
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomize_quicksort(A, p, r):
    """implementazione della versione randomizzata di quicksort

        Parametri:
        A (list): lista di numeri interi
        p (int): indice di inzio dell'array(o sottoarray)
        r(int): indice di fine dell'array(o sottoarray)
    """
    if p < r:
        q = randomize_partition(A, p, r)
        randomize_quicksort(A, p, q - 1)
        randomize_quicksort(A, q + 1, r)


def randomize_partition(A, p, r):
    """procedura partition

             Parametri:
                A (int): lista di numeri interi
                p (int): indice di inzio dell'array(o sottoarray)
                r(int): indice di fine dell'array(o sottoarray)

            Valore di Ritorno:
            int: indice del pivot
    """
    pivot = randint(p, r)
    A[r], A[pivot] = A[pivot], A[r]
    return partition(A, p, r)
