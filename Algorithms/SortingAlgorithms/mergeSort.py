def merge_sort(A, left, right):
    """
        Implementazione ricoriva di merge sort

        Argomenti:
            A (list):Array di elementi da ordinare
            left (int): indice dell'elemento di sinitra da cui si vuole ordinare l'array
            right (int): indice dell'elemento di destra fino a cui si vuole ordinare l'array
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, right, mid)


def merge(A, left_index, right_index, middle):
    # Copio i due array che voglio unire
    # il secondo parametro non è inclusivo, si deve incrementare di 1
    left_copy = A[left_index:middle + 1]
    right_copy = A[middle + 1:right_index + 1]

    # Inizializzazione dei contatori che si utilizzeranno
    # per tenere traccia dove si è in ciascun array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Itero tra le copie fino a che non termino gli elementi in una lista
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # Se la copia di sinistra ha un elemento più piccolo, lo si inserisce nella
        # lista ordinata e si inscrementa il contatore della lista di sinistra
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            A[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Altrimenti si fa la stessa cosa si sopra solo con l'array di destra
        else:
            A[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Indipendentemente da dove siamo incremento il
        # contatore della lista ordinata
        sorted_index = sorted_index + 1

    # Finiamo di iterare tra gli elementi della lista di sinistra
    # e della lista di destra e gli aggiungiamo all lista ordinata
    while left_copy_index < len(left_copy):
        A[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        A[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1