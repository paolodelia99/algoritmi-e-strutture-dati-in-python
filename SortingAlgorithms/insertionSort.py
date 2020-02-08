list = [25,36,85,4,56,95,22,65,45,87,31,2,15]

def insertionSort(list):
    orderList = initializeArray(list)
    for j in range(len(list)):
        if(j == 0):
            continue
        else:
            key = list[j]
            i = j-1
            while i>0 & list[i]>key:
                orderList[i+1] = list[i]
                i = i-1
            orderList[i+1] = key
    return orderList

def initializeArray(list):
    newList = []
    for i in range(len(list)):
        newList.insert(i, 0)
    return newList

def printArray(list):
    for item in list:
        print(item),

print('initial Array: ')
printArray(list)
print
print('final Array')
printArray(insertionSort(list))
