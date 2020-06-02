import numpy


def findMinCost(arr, m, n):
    if m == 0 or n == 0:
        return float('inf')

    if m == 1 and n == 1:
        return arr[0][0]

    return min(findMinCost(arr, m - 1, n), findMinCost(arr, m, n - 1)) + arr[m - 1][n - 1]


# solved with dp

def findMinCost2(arr):
    m = len(arr)
    n = len(arr[0])
    print(m,n)
    result = numpy.zeros((m, n))

    for i in range(m):
        for j in range(n):
            result[i][j] = arr[i][j]

            if i == 0 and j > 0:
                result[0][j] += result[0][j - 1]

            elif i > 0 and j == 0:
                result[i][0] += result[i - 1][0]

            elif i > 0 and j > 0:
                result[i][j] += min(result[i - 1][j], result[i][j - 1])

    return result[m - 1][n - 1]


op = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3]
]

print(findMinCost2(op))
