"""
In questo script ci sono i generatori causali di liste che ho utilizzato per testare gli
algoritmi di ordinamento e ricerca
"""
import random
from random import randint


def small_random_list_generator() -> list:
    """
        Valore di ritorno
            list: lista formata da un numero casuale di elementi (tra 10 e 22)
                 con elementi casuali tra 1 e 100
    """
    arr = []
    for i in range(randint(10, 22)):
        arr.append(randint(1, 101))
    return arr


def big_random_list_generator() -> list:
    """
        Valore di ritorno
            list: lista formata da un numero casuale di elementi (tra 10000 e 100000)
                 con elementi casuali tra 1 e 100000
    """
    arr = []
    for i in range(randint(10000, 100000)):
        arr.append(randint(1, 100000))
    return arr


def random_list_generator(dim: int, min: int, max: int) -> list:
    """
        Argomenti:
            dim (int): dimensione della lista
            min (int): minimo elemento del range dei numeri casuali da generare
            max (int): massimo elemento del range dei numeri casuali da generare

        Valore di ritorno:
            Ritorna lista di numeri interi di dimensione dim con numeri casuali compresi tra min e max
    """
    arr = []
    for _ in range(dim):
        arr.append(randint(min, max + 1))

    return arr


def zero_one_random_list_generator(n: int) -> list:
    """
        generatore di una lista di numeri compresi nell'intervallo [0,1)

        Argomenti:
            n (int): numero di elementi della lista

        Valore di ritorno:
            lista di dimensione n con numeri compresi tra 0 e 1
    """
    arr = []
    for i in range(n):
        arr.append(random.random())
    return arr
