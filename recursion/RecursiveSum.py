def func(array):
    def funcRec(array, acc):
        if (array == None or len(array) == 0):
            return acc
        head, tail = array[0], array[1:]
        acc.append(acc[-1] + tail[0])
        funcRec(tail, acc)

    return funcRec(array, [])


def func3(array):
    min_el = 1000000000
    for idx1, e1 in enumerate(array):
        acc = list()
        for idx2, el2 in enumerate(array):
            if idx1 is not idx2:
                if acc is not [] and len(acc) > 0:
                    lastEl = acc[-1]
                    acc.append(lastEl + array[idx2])
                else:
                    acc.append(e1 + array[idx2])
        sumsEl = sum(acc)
        if (sumsEl < min_el):
            min_el = sumsEl
    return min_el


# def func4(array, n, acc, min):
#     if (acc < min):
#         min = acc
#
#     if (n < 0):
#         return min
#
#     func4(array, n - 1, )


# func4([1, 3, 4, 5], 3, 0, 1000000)


# def func3():
#     if(len(a) > 3):
#         return acc

# print(func3([100, 250, 1000]))
# print(func([100, 250, 1000]))


def countWays(arr, n, target):
    if target == 0:
        return 1

    if (n < 0):
        return 0

    exclude = countWays(arr, n - 1, target)
    add = countWays(arr, n - 1, target - arr[n])
    sub = countWays(arr, n - 1, target + arr[n])
    return exclude + add + sub


print(countWays([5, 3, -6, 2], 3, 6))
