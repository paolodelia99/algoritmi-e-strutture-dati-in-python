from insertionSort import insertion_sort


def bucket_sort(A: list, n: int):
    """
        Impentazione di bucket sort

        Argomenti:
            A (list): lista di numeri da ordinare
            n (int): numero di bucket

        Valore di ritorno:
            lista ordinata
    """
    B = []  # lista di appoggio

    # Inizializzo l'array che andrà a contenere i bucket
    for i in range(n):
        B.append([])

    # Assegno a ogni bucket i suoi elementi
    for j in A:
        index_bucket = int(n * j)
        B[index_bucket].append(j)

    # ordina i singoli bucket
    for i in range(n):
        insertion_sort(B[i])

    # concateno i singoli bucket per ottenere
    # l'array ordinato
    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1

    return A
