def knapsack01(W, wt, val, n):
    """
        Soluzione dello zaino 0-1 utilizzando la programmazione dinamica

        Argomenti:
            W (int): peso totale
            wt (list): lista dei pesi degli oggetti
            val (list): lista dei valori degli oggetti
            n (int): numero degli oggetti

        Valore di Ritorno:
            massimo valore che si puo ottenere
    """
    # Tabella dove vado a memorizzare i valori migliori per ogni peso
    dp = [[0 for _ in range(W+1)] for x in range(n+1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1]
                               [w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
