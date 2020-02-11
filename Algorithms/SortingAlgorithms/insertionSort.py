"""Insertion Sort

Insertion sort è un algoritmo di ordinamento in place, cioè ordina
l'array senza doverne creare una copia, risparimando memoria.

Complessità temporale: O(n^2)
"""

def insertion_sort(list):
    for j in range(1,len(list)):

        key = list[j]
        i = j-1

        while i>=0 and list[i]>key:

            list[i+1] = list[i]
            i = i-1

        list[i+1] = key