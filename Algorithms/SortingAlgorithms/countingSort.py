def counting_sort(A, B, k):
    """Implementazione di Counting sort

        Parametri:
        A (list): lista di numeri interi da ordinare
        B (list): lista vuota che conterrà gli elementi di A ordinati a fine esecuzione
        k(int): massimo elemento di A
    """
    tmp_list = [] # lista temporenea di dimensione k
    for i in k:
        tmp_list[i] = 0
    for j in range(len(A)):
        tmp_list[A[j]] = tmp_list[A[j]] + 1
    for i in range(1, k):
        tmp_list[i] = tmp_list[i] + tmp_list[i - 1]
    for j in range(len(A), -1, -1):
        B[tmp_list[A[j]]] = A[j]
        tmp_list[A[j]] = tmp_list[A[j]] - 1
