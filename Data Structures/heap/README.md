# Heap

La struttura dati heap rappresenta un insieme dinamico
mediante un albero binario quasi completo le cui chiavi
soddisfano la "proprietà degli heap":

<br/>

se A è un genitore di B, allora la chiave di A è 
ordinata rispetto alla chiave di B conformemente alla relazione d'ordine applicata all'intero heap. 
 
<br/>
 
Di conseguenza, gli heap possono essere suddivisi in <b>"max heap"</b> e <b>"min heap"</b>.
 
<br/>
 
In un <b>"max heap"</b>, le chiavi di ciascun nodo sono sempre maggiori o uguali di 
quelle dei figli, e la chiave dal valore massimo appartiene alla radice.
  
<br/>
  
In un <b>min heap</b>, le chiavi di ciascun nodo sono sempre minori o uguali di quelle dei figli, e la chiave dal valore minimo appartiene alla radice.
  
  
![Heap](../../resources/imgs/MinHeapAndMaxHeap.png)

## Specifica

Le operazioni basilari e gli attributi che una stack possiede sono:

```text

boolean is_empty()
# restituisce true se la pila è vuot

push(Item v)
# inserisce v in cima alla pila

Item pop()
# estrae l'elemento in cima alla pila e lo restituisce al chiamante

top 
# attributo che è l'indice dell'elemento inserito più recente
```