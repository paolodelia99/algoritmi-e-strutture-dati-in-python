def counting_sort(A, B, k):
    """Implementazione di Counting sort

        Parametri:
        A (list): lista di numeri interi da ordinare
        B (list): lista vuota che conterrà gli elementi di A ordinati a fine esecuzione
        k(int): massimo elemento di A
    """
    C = [0] * (k + 1)  # lista temporenea di dimensione k

    for j in range(0, len(A)):
        C[A[j]] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    i = len(A) - 1
    while i >= 0:
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
        i -= 1