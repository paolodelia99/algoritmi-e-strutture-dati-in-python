# Sorting Algorithms

### QuickSort

Quicksort è un algoritmo di ordinamento ricorsivo in place.
E' basato sul paradigma divide et impera dal momento che: 
- <b>(Divide)</b> scompone ricorsivamente i dati da processare in sottoprocessi.La scomposizione viene effetuata dalla procedura 
<b>partiton(A, p, r)</b> che partiziona la lista A[p..r] in due sottoarray A[p..q-1] e A[q+1..r] tali che ogni elemento di A[p..q-1] sia minore o uguale ad A[q] che, a sua volta,
è minore o uguale a ogni elemento di A[q+1..r]. Questa procedura ritorna l'indice q.
- <b>(Impera)</b> oridna i due sottoarray A[p..q-1] e A[q+1..r] chiamando ricorsivmente quicksort
- <b>(Combina)</b> poichè i sottoarray sono già ordinati, non occorre alcun lavoro per combinarli: 
l'intero array A[p..r] è ordinato.

PSEUDO CODICE
```text
QUICKSORT(A, p, r)
if p < r
    q = PARTITION(A, p, r)
    QUICKSORT(A, p, q-1)
    QUICKSORT(A, q+1, r)
```

L'elemento chiave dell'algoritmo è la procedura PARTITION, che riarrangia il sottoarray A(p..r) sul posto.
```text
PARTITION(A, p, r)
x = A[r]
i = p - 1
for j = p to r - 1
    if A[j] <= x
        i = i + 1
        scambia A[i] con A[j]
scambia A[i+1] con A[r]
```

E' intuibile che il costo per trovare il pivot è di Θ(n)

#### Complessità computazionale

##### Caso pessimo 

Nel caso pessimo il vettore di dimensione <em>n</em> viene diviso 
in due sottovettori di dimensione 0 e <em>n</em> - 1
<br/>
Equazione di ricorrenza : 
T(n) = T(n − 1) + T(0) + Θ(n) = T(n − 1) + Θ(n) = Θ(n<sup>2</sup>)

##### Caso ottimo

Nel caso ottimo dato un vettore di dimensione <em>n</em>, questo viene sempre 
diviso in due sottoproblemi di <em>n</em>/2 dimensioni
<br/>
Equazione di ricorrenza : 
T(n) = 2T(n/2) + Θ(n) = Θ(n log<sub>2</sub> n)

##### Caso medio

Il tempo di esecuzione di quicksort è molto più vicino al caso migliore che al caso
peggiore. Questo perchè anche se l'algoritmo produca sempre partizionamenti 9 a 1, che a prima 
vista può sembrare molto sbilanciato, si ottiene dall'equazione di ricorrenza che:
<br/>
T(n) = T(n/10) + T(9n/10) + cn = Θ(n log<sub>2</sub> n)
<br/>
Questo succede anche con una ripartizione 99 a 1
<br/>
T(n) = T(n/100) + T(99n/100) + cn = Θ(n log<sub>2</sub> n)
<br/>
La ragione è che qualsiasi ripartizione con proporzionalità costante produce un albero di ricorsione di 
profondità  Θ(log<sub>2</sub> n), dove il costo in ogni livello è O(n). Il tempo di esecuzione è quindi
O(n log<sub>2</sub> n) quando la ripartizione ha proporzionalità costante.

...da finire

### Versione Randomizzata di Quicksort

A volte è possibile aggiunge la randomizzazione a un algoritmo per ottenre una buona prestazione 
attesa con tutti gli input. Però piuttosto che permutando esplicitamente l'input, si adotta un altro
metodo di randomizzazione, detto <b>campionamento casuale</b>, che consiste nella scelta di un 
pivot casuale ogni volta che la procedura PARTITION viene eseguita. Poichè il pivot viene scelto a 
caso, ci aspettiamo che la ripartizione dell'array di input sia ben bilancita in media. 

il nuovo RANDOMIZED-QUICKSORT è pittosto simile a QUICKSORT ma con delle piccole modifiche:

```text
RANDOMIZED-QUICKSORT(A, p, r)
if p < r
    q = RANDOMIZED-PARTITION(A, p, r)
    QUICKSORT(A, p, q-1)
    QUICKSORT(A, q+1, r)


RANDOMIZED-PARTITION(A, p, r)
i = RANDOM(p, r)
scambia A[r] con A[i]
return PARTITION(A, p, r)
```

#####  Tempo di esecuzione atteso

..da finire