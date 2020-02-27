def bubble_sort(list):
    """Bubble sort
    
    Argomenti:
        list {[int]} -- lista di numeri non ordinati
    """
    for i in range(0, len(list) - 1):
        for j in range(len(list) - 1, i, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]