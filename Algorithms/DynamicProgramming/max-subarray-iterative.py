"""
Kandane's Algorithm
Implementation of the iterative algorithm that finds the max sub array

"""
def max_subarray(numbers):
    """
        Algoritmo di Kandane per trovare maxsubaaray

        Argomenti:
            numbers (list): lista di numeri positivi e negativi

        Valore di ritorno:
            dict: dizionario che ha come chiavi best_sum, best_start, best_end
    """
    best_sum = 0
    best_start = best_end = 0
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the exsting sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1

    return dict({'bestSum': best_sum, 'bestStart': best_start, 'bestEnd': best_end})