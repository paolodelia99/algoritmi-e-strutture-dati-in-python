# Coda

Una coda è una struttura dati dinamica di tipo <b>FIFO</b>, First-in-First-out
(il primo in ingresso è l'ultimo ad uscire).

Il concetto di coda FIFO in informatica non è diverso dal concetto intutivo che si ha di coda,
funziona come le code che facciamo dal supermercato o dal parruchier: idealmente
si viene serviti nello stesso ordine in cui si è presentati.

![Queue](../../resources/imgs/Queue.png)

## Specifica

Le operazioni basilari e gli attributi che una coda possiede sono:

```text

boolean is_empty()
# restituisce true se la coda è vuota

enqueue(Item v)
# inserisce v infondo alla coda

Item dequeue()
# estrae l'elemento in testa alla coda e lo restituisce al chiamante

head 
# attributo che indica (o punta) all'inizio della coda

tail
# attributo che indica la prossima posizone in cui l'ultimo elemento che arriva alla coda 
# prende posto alla fine della coda
```

## Possibili implementazioni

### Liste monodirezionali

### Array Circolari