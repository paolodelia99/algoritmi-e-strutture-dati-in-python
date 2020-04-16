"""
Implementazione di due algoritmi per la moltiplicazione delle matrici quadrate:

- square_matrix_multiply

- square_matrix_multiply_recursive

"""


def square_matrix_multiply(matrix_1, matrix_2):
    n = len(matrix_1)
    # inizializzo la matrice finale
    matrix_3 = [[0 for i in range(n)] for j in range(n)]
    # itero tra le righe
    for i in range(0, n):
        # itero tra le colonne
        for j in range(0, n):
            for k in range(0, n):
                matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return matrix_3


def square_matrix_multiply_recursive(matrix_1, matrix_2):
    n = len(matrix_1)
    # inizializzo la matrice finale
    matrix_3 = [[0 for i in range(n)] for j in range(n)]
    if n == 1:
        matrix_3[0][0] = matrix_1[0][0]*matrix_2[0][0]
    else:
        matrix_3[0][0] = square_matrix_multiply_recursive(
            matrix_1[0][0], matrix_2[0][0])
        + square_matrix_multiply_recursive(matrix_1[0][1], matrix_2[1][0])

        matrix_3[0][1] = square_matrix_multiply_recursive(
            matrix_1[0][0], matrix_2[0][1])
        + square_matrix_multiply_recursive(matrix_1[0][1], matrix_2[1][1])

        matrix_3[1][0] = square_matrix_multiply_recursive(
            matrix_1[1][0], matrix_2[0][0])
        + square_matrix_multiply_recursive(matrix_1[1][1], matrix_2[1][0])

        matrix_3[1][1] = square_matrix_multiply_recursive(
            matrix_1[1][0], matrix_2[0][1])
        + square_matrix_multiply_recursive(matrix_1[1][1], matrix_2[1][1])

    return matrix_3
