def pascalTriangle(matrix, i, j):
    if (i == 1 or j == 1):
        return 1
    else:
        return pascalTriangle(matrix, i - 1, j - 1) + pascalTriangle(matrix, i - 1, j)


matrix = [
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
]

print(pascalTriangle(matrix, 5, 3))
