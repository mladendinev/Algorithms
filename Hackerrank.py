#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def isDivisible(a, b, k):
    return (a % k + b % k) == k or a + b == 0


def nonDivisbleSubsetRec(arr, k):
    if (len(arr) == 0 or arr is None):
        return set()

    head, rest = arr[0], arr[1:]
    result = nonDivisbleSubsetRec(rest, k)

    if len(result) > 1:
        for nonDivEl in result:
            if (nonDivEl + head) % k == 0:
                return result
        result.add(head)

    for el in rest:
        if (head + el) % k != 0:
            result.add(head)
            result.add(el)

    return result


def solution(a):
    m = {}
    for i in range(len(a)):
        m[a[i]] = i

    sorted_a = sorted(a)
    ret = 0

    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret += 1

            ind_to_swap = m[sorted_a[i]]
            m[a[i]] = m[sorted_a[i]]
            a[i], a[ind_to_swap] = sorted_a[i], a[i]
    return ret


def isValid(s):
    freq = {}
    for item in s:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    values = list(freq.values())
    freq.popitem()
    for idx, val in enumerate(values):

        n = set(values[:idx] + values[idx + 1:])
        if (len(n)) == 1:
            return "YES"
    return "NO"
    # raw_input()
    # a = [int(i) for i in raw_input().split(' ')]
    #
    # asc = solution(list(a))
    # desc = solution(list(reversed(a)))
    # print(min(asc, desc))


# for idx1 in range(len(rest)):
#     for idx2 in range(idx1 +1, len(rest)):
#         if(rest[idx1] + rest[idx2] % != 0):
#             continue


def nonDivisibleSubset(s, k):
    return nonDivisbleSubsetRec(s, k)


def maxPalindrome(s, l, r):
    churek = str(s)
    return churek[l - 1: r]


def isValid(x, y, rows, columns):
    return x >= 0 and x < rows and y >= 0 and y < columns


def gridSearch(matrix1, m1x, m1y, matrix2, m2x, m2y):
    rows = 4
    cols = 5

    if isValid(m1x, m1y, rows, cols) and matrix1[m1x][m1y] == matrix2[m2x][m2y]:
        return True

    if isValid(m1x, m1y, rows, cols):
        if gridSearch(matrix1, m1x + 1, m1y, matrix2, m2x, m2y) == True:
            return True
        if gridSearch(matrix1, m1x, m1y + 1, matrix2, m2x, m2y) == True:
            return True

    return False


def gridSearch2(matrix1, matrix2, R, C, r, c):
    for row in range(R):
        for column in range(C):
            if (matrix1[row][column] == matrix2[0][0]):
                if innerSearch(row, column, matrix1, matrix2, r, c, R, C):
                    return "YES"
    return "NO"


def innerSearch(startX, startY, matrix1, matrix2, r, c, R, C):
    for rowM2 in range(r):
        for colM2 in range(c):
            if startX + rowM2 < R and startY + colM2 < C and matrix1[startX + rowM2][startY + colM2] != matrix2[rowM2][
                colM2]:
                return False
    return True


def sumDigit(string):
    return sum([int(c) for c in string])

def superDigitSum(number):
    if (number < 10):
        return number

    return superDigitSum(s)




if __name__ == '__main__':
    k = 7
    s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]

    # result = nonDivisibleSubset(s, k)
    # print(len(result))
    # print(isDivisible(10, 20, 5))

    # matrix1 = [
    #     [0, 1, 3, 4, 8],
    #     [0, 5, 7, 8, 9],
    #     [1, 4, 5, 6, 10],
    #     [0, 0, 0, 0, 0]
    # ]
    #
    # matrix2 = [
    #     [5, 7, 8],
    #     [4, 5, 6]
    # ]

    # matrix1 = [
    #     [400453592126560
    #      114213133098692
    #      474386082879648
    #      522356951189169
    #      887109450487496
    #      252802633388782
    #      502771484966748
    #      075975207693780
    #      511799789562806
    #      404007454272504
    #      549043809916080
    #      962410809534811
    #      445893523733475
    #      768705303214174
    #      650629270887160
    #      ]
    # print(gridSearch(matrix1, 0, 0, matrix2, 0, 0))
    R = 4
    C = 6

    matrix1 = [
        [1, 2, 3, 4, 1, 2],

        [5, 6, 1, 2, 1, 2],

        [1, 2, 3, 6, 1, 2],

        [7, 8, 1, 2, 3, 4],
    ]
    matrix2 = [
        [1, 2],
        [3, 4]
    ]
    # print(gridSearch2(matrix1, matrix2, 4, 6, 2, 2))
    # print(superDigitSum(9875))
    # print(calculateSumDigits(11))
    print(m)
    # print(superDigit("9875", 1))
