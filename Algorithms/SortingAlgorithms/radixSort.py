from countingSort import counting_sort


def counting_sort(arr, exp1):
    """
        Counting sort riemplementato per radix sort

        Parametri:
            arr (list): lista da ordinare
            exp1 (int): cifra corrente del numero
    """
    n = len(arr)

    # Array di appoggio della stessa dimensione di arr
    output = [0] * (n)

    # inizializzo count array
    count = [0] * (10)

    # memorizzo le occorenze in count
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    # Modifico count[i] in modo tale che contenga quanti elementi di
    # input siano minori o uguali a i
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Costruzione dell'array output
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copia array output in arr[],
    # ora arr[] è un array ordinato
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr: list):
    """
        Implementazione dell'algoritmo radix sort

        Argomenti:
            arr (list): lista di numeri interi da ordinare
    """
    # Trovo l'elemento più grande per conoscere il massimo numero di cifre
    max1 = max(arr)

    # Applica counting sort per ogni cifra. Nota che invece di
    # passare la cifra a counting sort, è passato exp. dove
    # exp è 10^i dove i è la cifra corrente
    exp = 1
    while max1 / exp > 0:
        counting_sort(arr, exp)
        exp *= 10
