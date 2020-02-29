# Linked List (o liste concatenate)

Una **lista concatenata** è una struttura dati dinamica i cui oggetti sono disposti in ordine lineare.
Consiste di una sequenza di nodi, ognuno contenente campi di dati arbitrari ed uno o due riferemienti
(*link*) che puntano al nodo successivo e/o precedente. 

Le lista concatenate permettono l'inserzione e la rimozione di nodi in ogni punto 
della lista in tempo costante, ma non permettono l'accesso casuale, solo quello *sequenziale*. 

Le liste concatenate possono essere implementate in vari modi: 

- possono essere ***bidirezionali*** o ***monodirezionali***
- possono essere ***circolari*** o ***non circolari***
- possono la ***sentinella*** oppure no 
 
![Linked-List](../../resources/imgs/liste-concatenate.png)

## Specifica

### Lista concatenata bidirezionale

Specifica della classe node che poi verrà utilizzata nella linked list
```text
next
# attributo che memorizza il puntatore all'elemento succesivo

prev
# a  attributo che memorizza il puntatore all'elemento succesivo

v
# oggeto che viene memorizato nel node

```

```text
head
# puntatore al primo nodo della lista

tail
# puntatore all'ultimo elemento della lista

isEmpty()
# metodo che ritorna vero se la lista è vuota

read(Node n)

write(Node n,Object v)

next(Node n)

prev(Node n)

remove(Node n)

insert(Node n,Object v)

```