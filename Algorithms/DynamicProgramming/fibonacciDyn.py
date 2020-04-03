def fibo(n):
    """
        Implementazione del algoritmo di calcolo della sequenza di fibonacci con la programmazione dinamica

        Argomenti:
            n (int): -nesimo numero di fibonacci

        Valore di ritorno:
            fib[n] ennesimo numero della sequenza di fibonacci`
    """
    fib= [0,1]

    for i in range(2,n):
        fib[n] = fib[n-1] + fib[n-2]

    return fib[n]