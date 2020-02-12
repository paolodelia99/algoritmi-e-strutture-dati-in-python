# Testing Algoritmi di ordinamento

Lo schema generale che ho seguito per testare gli algoritmi di ordinamento è descritto dal seguente codice:

```python
from package import algoritmo_di_sorting_da_testare

list_ = [5,2,4,6,1,7,3]
# creo una copia della lista che andrò ad ordinare con l'algoritmo di ordinamento che voglio testare
sorted_list = list_.copy()
# la ordino con l'algoritmo da testare
algoritmo_di_sorting_da_testare(sorted_list)
# ordino con la funzione sort() la lista inziale
list_.sort()

def test_algo():
    """
        nel test creo uno zip formato dalle due liste ordinate
        e controllo se ogni elemento della prima lista è uguale al
        corrispettivo elemento della seconda lista
    """
    assert all([a == b for a,b in zip(list_,sorted_list)])
```

Seguendo questo schema generale quello che ho fatto è stato di effettuare tre tipi di test: 

- il primo test l'ho effetuato su una semplice lista formata da numberi tra l'1 e il 10, formata al più da 10 elementi. Questa lista l'ho chiamata sample_list, 
mentre il corrispettivo test l'ho chiamato test_sample_list. Per verificare se l'algoritmo da testare è corretto ho operato utilizzando lo schema generale sopra descritto

- il secondo test l'ho effettuato su tre liste create casualmente col metodo <b>randint</b> di <b>random</b>, con un range di numeri che va da 1 a 100, 
ciasciuna con un numero di elementi che va da 10 a 22 ( dato che anche il numero di elementi della lista è generato casualmente)
Per verificare la corretezza dell'algoritmo da testare operato utilizzando lo schema generale sopra descritto per ciascuna lista creata

- il testo test l'ho effetuato su liste veramente grandi...(da finire)