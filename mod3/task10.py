def fill_matrix(size):
    matrix = [[0] * size for i in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            matrix[i][j] = j + 1
    return matrix


def transpose_matrix(m):
    size = len(m)
    res_matrix = [[0] * size for i in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            res_matrix[i][j] = m[j][i]
    return res_matrix


def print_matrix(matrix):
    size = len(matrix)
    s = []
    for i in range(size):
        for j in range(size):
            s.append(str(matrix[i][j]))
        print(', '.join(s))
        s = []
    print()


size = int(input())
matrix = fill_matrix(size)
print_matrix(matrix)
print_matrix(transpose_matrix(matrix))
