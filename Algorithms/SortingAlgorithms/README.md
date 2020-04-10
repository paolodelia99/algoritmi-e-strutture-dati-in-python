# Sorting Algorithms

Un classico problema algoritmico consiste di ordinare una sequenza di *n* elementi. 
Per poter ordinare tale le sequenza è necessario che gli elementi appartengano tutti ad un insieme dove è definita una relazione d'ordine; ossia, presi due elementi a scelta, deve sempre essere possibile accertare quale venga prima e quale dopo. Dunque per poter ordinare è necessario che esista:

- Una chiave per ogni elemento
- Un metodo (che solitamente restituisce un intero) che definisca l'ordine tra due elementi

## Proprietà degli algoritmi di ordinamento

### Stabilità

Un algoritmo di ordinamento si dice stabile se in presenza di due elementi con la medesima chiave (due acquisti nella stessa data ad esempio) non modifichi l'ordine con cui i due elementi si presentavano prima dell'ordinamento.

### Sul posto (o "in loco")

Un algoritmo di ordinamento su array si dice sul posto se in ogni dato istante al più è allocato un numero costante di variabili, oltre all'array da ordinare: un algoritmo, quindi, è sul posto se non utilizza array di supporto.

## Algoritmi

- **[Bubble sort](#bubble-sort)**
- **[Selection sort](#selection-sort)**
- **[Insertion sort](#insertion-sort)**
- **[Merge sort](#merge-sort)**
- **[Quick sort](#quicksort)**
- **[Counting sort](#counting-sort)**

### Bubble sort

Il bubble sort o bubblesort è un semplice algoritmo di ordinamento per ordinare array.
L'algoritmo deve il suo nome al modo in cui gli elementi vengono ordinati in una lista: quelli più piccoli "risalgono" 
verso un'estremità della lista, mentre quelli più grandi "affondano" verso l'estremità opposta della lista, come le bolle in un bicchiere di spumante.

#### Descrizione

Ogni coppia di elementi adiacenti viene comparata e invertita di posizione se sono 
nell'ordine sbagliato. L'algoritmo continua nuovamente a ri-eseguire questi passaggi 
per tutta la lista finché non vengono più eseguiti scambi, situazione che indica che la 
lista è ordinata.

#### Pseudo-codice

```text

BUBBLE-SORT(A)
    for i = 0 to A.length
        for j = A.length downto i +1 
            if A[j] < A[j-1]
                scambia A[j] con A[j-1]

```

- **Compessità Temporale**:
   - Caso Peggiore O(n<sup>2</sup>)
   - Caso Medio O(n<sup>2</sup>)
   - Caso Ottimo O(n<sup>2</sup>)

---

### Selection Sort

Selection sort è un algoritmo di ordiameneto che opera **in place**
 ed in modo simile all'**insertion sort**. L'algoritmo è di tipo **non adattivo**, 
 ossia il suo tempo di esecuzione non dipende dall'input ma dalla dimensione dell'array.

#### Come Funziona

L'algotimo seleziona di volta in volta il numero minore nella sequenza di partenza e lo sposta
nella sequenza ordinata. Quello che selection sort fa è quindi di dividere la sequenza in due parti:
la sottosequenza ordinata, che occupa le prime posizioni dell'array, e la sottosequenza da ordinare,
che occupa la parte restante dell'array.

#### Pseudocodice
```text
SELECTION-SORT(A)
    n = A.length
    for i = 0 to n
        posmin = i
        for j = i+1 to n
            if A[j] < A[posmin]
                posmin = j
        if posmin != i
            scambia A[i] con A[posmin]  
```

- **Compessità Temporale**:
   - Caso Peggiore O(n<sup>2</sup>)
   - Caso Medio O(n<sup>2</sup>)
   - Caso Ottimo O(n<sup>2</sup>)

---

### Insertion sort

Insertion sort è un algoritmo di ordinamento che opera **in place**, è un algoritmo
relativamente semplice per oridinare un array.

#### Come funziona

Come selection sort insertion sort divide l'array inziale in due sottoarray: il 
primo sottoarray è quello già ordinato, mentre il secondo sottoarray è quello da ordinare.
All'inizio la prima sottosequenza è già ordinata, in quanto è composta da un solo elemento,
all'*k*-esima iterazione, la sequenza ordinata contiene *k* elementi. In ogni iterazione, 
viene rimosso un elemento della sottosequenza da ordinare e *inserito* nella sequenza ordinata.


#### Pseudocodice

```text
INSERTION-SORT(A)
    for j = 2 to A.length
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
```

- **Compessità Temporale**:
   - Caso Peggiore O(n<sup>2</sup>)
   - Caso Medio O(n<sup>2</sup>)
   - Caso Ottimo O(n)
   
### Merge Sort 

**Merge Sort** è un algoritmo di ordinamento basato su confronti che utlizza un processo di
risoluzione **ricorsivo**, sfruttando la tecnica **Divide et Impera**.


#### Come funziona

Concettualmente, l'algoritmo funziona nel seguente modo:

* Se la sequenza da ordinare ha lunghezza 1, è già ordinata. Altrimenti:
* La sequenza viene divisa (*divide*) in due metà( se la sequenza contiene un 
numero dispari di elementi, viene divisa in due sottosequenza dove la prima avrà un
elemento in più rispetto alla seconda)
* Ognuna di queste sottosequenze viene ordinata, applicando **ricorsivamente** l'algoritmo(*impera*)
* Le due sottosequenze ordinate vengono unite (*combina*). Per fare questo, si estrae ripetutamente il
minimo delle sottosequenza e lo si pone nella sequenza in uscita, che risulterà ordinata.

####Pseudocodice

```text
MERGE-SORT(A,p,r)
    if p < r
        q = floor((p+r)/2)
        MERGE-SORT(A,p,q)
        MERGE-SORT(A,q+1,r)
        MERGE(A,p,q,r)
```

```text
MERGE(A,p,q,r)
    num_1 = q - p + 1
    num_2 = r - q
    L = new Array(num_1+1)
    R = new Array(num_2+1)
    for i = 1 to num_1
        L[i] = A[p+i-1]
    for j = 1 to num_2
        R[j] = A[q+j]
    L[num_1+1] infinity
    R[num_2+1] = infinity
    i = 1 
    j = 1
    for k = p to r
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else if A[k] = R[j]
            j = j + 1
```

- **Compessità Temporale**:
   - Caso Peggiore O(n log<sub>2</sub>n)
   - Caso Medio O(n log<sub>2</sub>n)
   - Caso Migliore O(n log<sub>2</sub>n)
   

---

### Bitonic Sort

- [ ] todo

---

### QuickSort

Quicksort è un algoritmo di ordinamento **ricorsivo in place non stabile**. Appartiene alla classe degli algoritmi **divide et impera**,
dal momento che scompone ricorsivamente i dati da processare in sottoprocessi.

#### Come funziona

I passi che quicksort compie sono i seguenti: 
- <b>(Divide)</b> scompone ricorsivamente i l'array da ordinare in sottoarray.La scomposizione viene effetuata dalla procedura 
<b>partiton(A, p, r)</b> che partiziona la lista A[p..r] in due sottoarray A[p..q-1] e A[q+1..r] tali che ogni elemento di A[p..q-1] sia minore o uguale ad A[q] che, a sua volta,
è minore o uguale a ogni elemento di A[q+1..r]. Questa procedura ritorna l'indice q.
- <b>(Impera)</b> oridna i due sottoarray A[p..q-1] e A[q+1..r] chiamando ricorsivmente quicksort
- <b>(Combina)</b> poichè i sottoarray sono già ordinati, non occorre alcun lavoro per combinarli: 
l'intero array A[p..r] è ordinato.

#### Pseudocodice

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

### Counting Sort

Il **Counting sort** è un algoritmo di ordinamento per valori numerici con complessità linieare. 
L'algoritmo presuppone che ciascuno degli *n* elementi di input sia un numero intero compreso nell'intervallo
da 0 a *k*, per qualche intero *k*.

#### Come funziona

L'algoritmo utilizza un'array di appoggio, di dimensione pari all'intervallo dei valori, dove va a memorizzare tutte le occorenze di ciscuna valore presente 
nell'array da ordinare.Successivamente eseguendo una scansione di C si modifica il valore dei
suoi elementi, assegnando ad ogni ci il numero di elementi di A minori o uguali ad i.
Infine, con una terza ed ultima scansione dell’array C si costruisce un nuovo array B ordinato
#### PseudoCodice

```text
// A array da ordinare
// B array A ordinato 
// k valore massimo di A
COUNTING-SORT(A,B,k)
    C = new Array(k)  //inizializzazione dell'array di appoggio
    for j = 1 to A.length
        C[A[j]] = C[A[j]] + 1

    for i = 1 to k
        C[i] = C[i] + C[i + 1]

    for j = A.length downto 1
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] -1
```

- **Compessità Temporale**:
   - Caso Peggiore O(k + n) se k ∉ O(n), 
                   θ(n)     se k ∈ O(n)
   - Caso Medio O(k + n) se k ∉ O(n), 
                θ(n)     se k ∈ O(n)
   - Caso Migliore O(k + n) se k ∉ O(n), 
                   θ(n)     se k ∈ O(n)
                   
                   
### Radix sort

Radix sort è un algoritmo di ordinamento che non utilizza i confronti. L'algoritmo 
utilizza un procedimento controintuitivo per l'uomo, ma pià facilmente implementabile. Esegue gli ordinameni 
per posizione della cifra ma partedno della cifra meno significativa.


#### Pseudocodice

```text
RadixSort(A,d)
    for i = 1 to d
        usa un ordinamento stabile per ordinare l'array A sulla cifra i
```

- **Complessità Temporale**:
    - se utilizza counting sort come algoritmo di ordinamento stabile θ(d(k+ n)), dove *d* è il numero di cifre dell'elemento massimo dell'array
    
### Bucket sort

Bucket sort è un algoritmo di ordinamento non in loco che presuppone che l'input sia estratto 
da una distribuzione uniforme. Come counting sort, bucket sort  è veloce perchè fa un ipotesi sull'input: 
esso suppone che l'input sia generato da un processo casuale che distribuisce gli elementi uniformemente e indipendentemente
nell'intervallo [0,1). 

#### Come funziona

Bucket sort divide l'intervallo [0,1) in *n* sottointervalli della stessa dimensione, chiamati **bucket**(cesto). Ciascun 
valore dell'array è inserito nel bucket a cui appartiene, i valori all'interno di ogni bucket vengono ordinati e l'algoritmo si conclude con 
la concatenazione dei valori contenuti nei bucket. Dato che l'algoritmo assume che l'input sia uniformemente e indiependentemente
nell'intervallo [0,1), non si aspetta che molti numeri vadano a finire nello stesso bucket.

#### Pseudocodice

    bucketSort(A,n)
        B = new Array(n-1)
        
        //Crea buckets
        for i = 0 to n
            B[i] = []
        
        //Inserisce ciascun elemento nel proprio bucket di appartenenza
        for j = 0 to A.length
            index_bucket = Math.floor(A[j])
            B[index_bucket = A[j]
            
        //Ordina i singoli Bucket 
        for i = 0 to n
            insertionSort(B[i])
             
        //concatena i bucket
        k = 0
        for i = 0 to n
            for j = 0 to B[i].length
                A[k] = B[i][j]
                k++
        
        return A

- **Compessità temporale**
    - Caso Peggiore: O(n<sup>2</sup>)
    - Caso Medio: O(n + (n<sup>2</sup>/k) + k) dove *k* è il numero di bucket, se k = θ(n) allora il tempo diventa O(n) 