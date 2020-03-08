from random import randint


def randomize_in_place(A):
    n = len(A)
    for i in range(0, n):
        random_index = randint(0, n - 1)
        A[i], A[random_index] = A[random_index], A[i]

    return A