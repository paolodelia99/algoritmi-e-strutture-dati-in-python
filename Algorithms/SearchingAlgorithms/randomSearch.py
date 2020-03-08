import random
from random import randint


def random_search(list, element):
    """ random search

        Parametri:
            list_ (list): lista di numeri interi
            element (int): elemento da trovare

        Valore di Ritorno:
            int: indice dell'elemento all'interno dell'array, altrimenti se non è presente ritorna -1
    """
    counter_list = [0] * len(list)
    while not check_list_elements(counter_list):
        random_index = random.randint(0, len(list) - 1)
        if list[random_index] == element:
            return random_index
        else:
            counter_list[random_index] = True

    return -1


def las_vegas_algorithm(list_, element):
    """Las vegas algorithm

        Parametri:
            list_ (list): lista di numeri interi
            element (int): elemento da trovare

        Valore di Ritorno:
            int: indice dell'elemento all'interno dell'array, altrimenti se non è presente ritorna -1
    """
    randomIndex = randint(0, len(list_))
    while list_[randomIndex] != element:
        randomIndex = randint(0, len(list_))

    return randomIndex


def search_MA(list_, element, n_iteration):
    """Algoritmo di montecarlo

     Parametri:
         list_ (list): lista di numeri interi
         element (int): elemento da trovare
         n_iteration (list): numero massimo di iterazioni

     Valore di Ritorno:
         int: indice dell'elemento all'interno dell'array, altrimenti se non è presente ritorna -1
    """
    for i in range(0, n_iteration):
        random_index = randint(0, len(list_))
        if list_[random_index] == element:
            return random_index

    return -1


def check_list_elements(list):
    """Check if the list is made all by Trues
    
    Arguments:
        list {[bool]} -- list that stores old indexes choose by the random number
    
    Returns:
        bool -- if the list is made by all true returns true else false
    """
    for i in range(0, len(list)):
        if list[i] == False:
            return False

    return True
