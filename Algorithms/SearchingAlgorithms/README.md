# Searching Algorithm

- **[Ricerca Binaria](#riceca-binaria-o-dicotomica)**
- **[Ricerca Lineare](#riceca-lineareo-sequenziale)**
- **[Jump Search](#jump-search)**
- **[Interpolation Search](#iterpolation-search)**
- **[Random Search](#random-search)**
- **[Las vegas Algorithm](#las-vegas-algorithm)**

### Riceca Binaria (o Dicotomica)

La ricerca binaria( o ricerca dicotomica ) è un algoritmo di ricerca che indice 
di un  determinato valore presente in un insieme ordinato di dati.
<br/> 
A diferrenza della ricerca sequenziale, la ricerca binaria effetua molti meno confronti, dato che 
sfruttando l'ordinamento dell'array, dimezza l'intervallo di ricerca ad ogni passaggio.

#### Come funziona

L'idea dell'algoritmo si rifa al metodo che si usa per trovare una parola su un dizionario:
sapendo che il vocabolario è ordinato alfabeticamente, l'idea è quella di iniziare
la ricerca non dal primo elemento, ma da quello centrale, cioè a metà del dizionario.
Si confronta questo elemento con quello cercato:

- se corrisponde, la ricerca termina indicando che l'elemento è stato trovato;

- se è superiore, la ricerca viene ripetuta sugli elementi precedenti (ovvero sulla prima metà del dizionario), scartando quelli successivi;

- se invece è inferiore, la ricerca viene ripetuta sugli elementi successivi (ovvero sulla seconda metà del dizionario), scartando quelli precedenti.

Se si arriva al punto che tutti gli elementi vengono scartati, la ricerca termina indicando che il valore non è stato trovato.

#### versione iterativa

#### Pseudocodice

```text
BINARY-SEARCH(A,p,r,el)
  if el < A[p] or el > A[r]
    return -1

  while p <= r
    mid = (p+r)//2
    if A[q] == el
        return q
    
    if A[q] > el
        r = q - 1
    else 
        p = q + 1

  return -1 
```

#### versione ricorsiva

#### Pseudocodice

```text
BINARY-SEARCH(A,p,r,el)
    if p > r
        return -1 
    
    if el < A[p] or el > A[r]
        return -1 
    
    mid = (p+r)//2
    if A[mid] == el
        return mid
    else if A[mid] > el
        return BINARY-SEARCH(A,p,q-1,el)
    else
        return BINARY-SEARCH(A,q+1,r,el) 
```

- **Complessità Temporale**:

  - Caso Peggiore: O(log<sub>2</sub>(n))
  - Caso Medio: O(log<sub>2</sub>(n))
  - Caso Migliore: O(1)
  
### Riceca Lineare(o Sequenziale)

In informatica la ricerca sequenziale (o ricerca lineare) è un algoritmo utilizzabile per 
trovare un elemento in un insieme non ordinato.

#### Come funziona

L'algoritmo controlla in sequenza gli elementi dell'insieme, arrestandosi quando ne trova 
uno che soddisfa il criterio di ricerca; non potendosi avvalere di alcun ordinamento tra 
gli elementi, l'algoritmo può concludere con certezza che l'insieme non contiene alcun 
elemento corrispondente solo dopo averli verificati tutti, richiedendo pertanto un numero di controlli, nel caso peggiore, pari alla cardinalità dell'intero insieme.

#### Pseudocodice
```text
LINEAR-SEARCH(A,el)
    for i in A.length
        if A[i] == el
            return i

    return -1 
```

- **Complessità computazionale**
    - Caso Peggiore: O(n)
    - Caso Medio: O(n)
    - Caso Migliore: O(1)

### Jump Search 

Come la ricerca binaria, jump search è un algoritmo di ricerca in una sequenza **ordinata**.
L'idea è quella di controllare pochi elementi saltando in avanti con passi fissi o saltando alcuni 
elementi al posto della ricerca di tutti gli elementi.


#### Come funziona

Per esempio, consideriamo di avere una lista *A* di lunghezza *n* e un sequenza fissa di passi da saltare
di lunghezza *m* (ovviamente con m<n). Ora cerchiamo tra gli indici 
*A*[0],*A*[*m*],*A*[2*m*],...*A*[k*m*] e così via. Una volta che si è
trovato l'intervallo *A*[k*m*] < x < *A*[(k+1)*m*] si effetua la ricerca 
sequenziale dall'indice k*m* per trovare l'elemento *x*.
 
Il valore ottimale di *m* è √*n* dove *n* è lunghezza della lista *A*.
Poiché entrambi i passaggi dell'algoritmo esaminano, al massimo, √n elementi che l'algoritmo viene eseguito nel tempo O (√n)

 
#### Pseudocodice

```text 
JUMP-SEARCH(A,el)
    n = A.lenght
    m = floor(sqrt(n))     // passi da saltare
    prev = 0
                      
    // trova il blocco dove l'elemento è presente
    while A[min(m,n)-1] < x
        prev = m 
        m = floor(sqrt(n))
        if prev >= n
            return -1
    
    //Ricerca linare per trovare el in blocco
    // che inizia con prev    
    while A[prev] < el
        prev = prev +1    
        
        // se abbiamo raggiunto fine del blocco 
        // o la fine dell'array ritorna -1 
        if prev == min(m,n)
            return -1
    
    // Se l'elemento è stato trovato
    if arr[prev] == el
        return prev
    
    return -1
```

- **Complessità Computazionale**:
    - Caso Peggiore: O(√n)
    - Caso Medio: O(√n)
    - Caso Migliore: O(1)


### Iterpolation Search

L'interpolation search è un algoritmo di ricerca di un dato valore chiave in un array ordinato tramite gli stessi valori delle chiavi.

#### Come funziona
Per trovare la soluzione da cercare utilizza la seguente formula:
```text 
pos = low + [ (el-arr[low])*(high-low) / (arr[high]-arr[low]) ]
dove
arr[]  èl'array dove l'elemento devo essere cercato
el è l'elemento che deve essere cercato
low è l'indice di partenza dell'array
high è l'indice di fine dell'array
```                               

Quello che fa l'algoritmo è di utilizzare un ciclo che el sia compreso tra low e high
e aggiorna  la variabile pos con la formula sopra indicata. Se elemento è trovato in pos
termina l'esecuzione. Se l'elemento è minore di A[pos], aggiorna pos nel sottoarray di sinistra
altrmineti calcola pos per il sottoarray di destra. Ripete questo ciclo fino a che 
non trova l'elemento o is sottoarray si riduce a dimensione pari a 0.

#### Pseudocodice

```text 
INTERPOLATION-SEARCH(A,el)
    n = A.length
    low = 0
    high = n - 1
               
    while low <= high and el >= A[low] and el <= A[high]
        if low == high
            if A[low] == el
                return low
            return -1
        

        pos = low + int(((float(high-low)/(A[high]-A[low]))*(el-A[low])))
        
        if A[pos] == x 
            return pos

        if A[pos] < x
            low = pos + 1
        else
            high = pos - 1

    
    return -1   
```


- **Complessità computazionale**
    - Caso Peggiore: O(n)
    - Caso Medio: log(log(n)) 
    - Caso Migliore: O(1)

### Ricerca utilizzando la casualità

#### Randomized Select

- [ ] todo (readme)

#### Random Search
The Random search algorithm is a search algorithm that find an element in a list
by choosing a random index every time until the all the indexes are choosen or when the
element is found

expected execution time: O(ln n) 

#### Las vegas Algorithm

L'algoritmo di Las Vegas è un algoritmo di ricerca randomizzato che da sempre la risposta corretta; cioè
ritorna il l'indice corretto o chi informa del suo fallimento nel trovare l'elemento da cercare.
Tuttavia, il tempo di esecuzione dell'Algoritmo di Las vegas dipende dall'input

#### ALgoritmo di Monte Carlo per la ricerca di un elemento


### Scamble Search