# Searching Algorithm

### Binary Search

La ricerca binaria( o ricerca dicotomica ) è un algoritmo di ricerca che indice 
di un  determinato valore presente in un insieme ordinato di dati.
<br/> 
A diferrenza della ricerca sequenziale, la ricerca binaria effetua molti meno confronti, dato che 
sfruttando l'ordinamento dell'array, dimezza l'intervallo di ricerca ad ogni passaggio.
<br/>
L'idea dell'algoritmo si rifa al metodo che si usa per trovare una parola su un dizionario:
sapendo che il vocabolario è ordinato alfabeticamente, l'idea è quella di iniziare
la ricerca non dal primo elemento, ma da quello centrale, cioè a metà del dizionario.
Si confronta questo elemento con quello cercato:

- se corrisponde, la ricerca termina indicando che l'elemento è stato trovato;

- se è superiore, la ricerca viene ripetuta sugli elementi precedenti (ovvero sulla prima metà del dizionario), scartando quelli successivi;

- se invece è inferiore, la ricerca viene ripetuta sugli elementi successivi (ovvero sulla seconda metà del dizionario), scartando quelli precedenti.

Se si arriva al punto che tutti gli elementi vengono scartati, la ricerca termina indicando che il valore non è stato trovato.

#### versione iterativa

#### versione ricorsiva

Caso temporalemente peggiore: O(log<sub>2</sub>(n))
Caso medio temporalmente: O(log<sub>2</sub>(n))

### Deterministic Search

### Ricerca utilizzando la casualità

#### Random Search
The Random search algorithm is a search algorithm that find an element in a list
by choosing a random index every time until the all the indexes are choosen or when the
element is found

expected execution time: O(ln n) 

#### Las vegas Algorithm

L'algoritmo di Las Vegas è un algoritmo di ricerca randomizzato che da sempre la risposta corretta; cioè
ritorna il l'indice corretto o chi informa del suo fallimento nel trovare l'elemento da cercare.
Tuttavia, il tempo di esecuzione dell'Algoritmo di Las vegas dipende dall'input

In computing, a Las Vegas algorithm is a randomized algorithm that always gives correct results; that is, it always produces the correct result or it informs about the failure. However, the runtime of a Las Vegas algorithm differs depending on the input

#### ALgoritmo di Monte Carlo per la ricerca di un elemento


### Scamble Search