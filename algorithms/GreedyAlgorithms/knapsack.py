def fractional_knapsack(value, weight, capacity):
    """
        Algoritmo che risolve il problema dello zaino frazionario con l'approccio Greedy

        Argomenti:
            value (list): lista dei valori degli oggetti
            weight (list): lista dei pesi degli oggetti
            capacity (int): capacità dello zaino

        Valore di ritorno
            (max_value, fractions) tupla contenente il massimo valore ottenibile e le corrispettive frazioni dei oggetti presi
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v / w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break

    return max_value, fractions
