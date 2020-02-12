# Sorting Algorithms

### QuickSort

Quicksort è un algoritmo di ordinamento ricorsivo in place.
E' basato sul paradigma divide et impera dal momento che scompone ricorsivamente
i dati da processare in sottoprocessi.
<br/> 
La scomposizione viene effetuata dalla procedura 
<b>partiton(A, p, r)</b> che partiziona la lista A(p..r) in due sottoarray
A(p..q-1) e A(q+1..r) tali che ogni elemento di A(p..q-1) sia minore o uguale ad A[q] che, a sua volta,
è minore o uguale a ogni elemento di A(q+1..r)
