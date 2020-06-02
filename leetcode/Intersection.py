def intervalIntersection(A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """

    pointerA = 0
    pointerB = 0

    while pointerA < len(A) and pointerB < len(B):
        fromA = A[pointerA][0]
        toA = A[pointerA][1]

        fromB = B[pointerB][0]
        toB = B[pointerB][1]

        intersection = set(range(fromA, toA + 1)).intersection(set(range(fromB, toB + 1)))
        print(intersection)

        pointerA += 1
        pointerB += 1


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
intervalIntersection(A, B)