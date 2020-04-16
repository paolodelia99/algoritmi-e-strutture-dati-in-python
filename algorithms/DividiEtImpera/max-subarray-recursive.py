import random
import math
""" 
Implementation of the recursive algorithm that finds the max sub array

"""

list = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]


def findMaxSubArray(A, low, high):

    if low == high:
        return low, high, A[low]
    else:

        mid = int(math.floor((low+high)/2))
        (leftLow, leftHigh, leftSum) = findMaxSubArray(A, low, mid)
        (rightLow, rightHigh, rightSum) = findMaxSubArray(A, mid+1, high)
        (crossLow, crossHigh, crossSum) = findMaxCrossingSubArray(A, low, mid, high)

        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum


def findMaxCrossingSubArray(A, low, mid, high):

    leftSum = -1000
    sum = 0
    maxLeft, maxRight = (0, 0)
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i

    rightSum = -1000
    sum = 0
    for j in range(mid+1, high+1):
        sum = sum + A[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j

    return (maxLeft, maxRight, leftSum+rightSum)


# Check if the algo is working with the default list
print('The default list is:')
print(list)
print('max sub array is ')
print(findMaxSubArray(list, 0, len(list)-1))

# Test with three different Random list
list1 = []
list2 = []
list3 = []

for i in range(random.randint(10, 22)):
    list1.append(random.randint(-101, 101))

for i in range(random.randint(10, 22)):
    list2.append(random.randint(-101, 101))

for i in range(random.randint(10, 22)):
    list3.append(random.randint(-101, 101))

# Check if is working also with the random lists
print('Random Lists')
print('List n1:')
print(list1)
print('max subArray in list 1:')
print(findMaxSubArray(list1, 0, len(list1)-1))

print('List n2:')
print(list2)
print('max subArray in list 3:')
print(findMaxSubArray(list2, 0, len(list2)-1))

print('List n3: ')
print(list3)
print('max subArray in list 3:')
print(findMaxSubArray(list3, 0, len(list3)-1))
