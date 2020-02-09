"""Selection sort
Selection sort is an in-place comparison sorting algorithm.
Is inefficent for large lists, and generally performs worse that the similar insertion sort.


time complexity: O(n^2)
"""

def selecion_sort(list):
    for j in range(0,len(list)-1):
        currentMin = j
        for i in range(j+1,len(list)):
            if list[i] < list[currentMin]:
                currentMin = i 
            if currentMin != j:
                list[j],list[currentMin] = list[currentMin],list[j]

#  Default list
list = [4,8,2,9,10,2,5,6,1]
print(f'initial list {list}')
selecion_sort(list)
print(f'sorted list: {list} ')