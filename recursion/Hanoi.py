import itertools


def move(f, t):
    print("Move disc from {} to {}".format(f, t))


def hanoi(n, f, helper, target):
    if n == 0:
        pass
    else:
        hanoi(n - 1, f, target, helper)
        move(f, target)
        hanoi(n - 1, helper, f, target)


def combinationTupple(l):
    res = list(itertools.combinations(l, 2))
    print(res)
    return res


def recursiveSum(l):
    def recursiveSum(l, start):
        res = list()
        if (start > len(l) - 1):
            return res
        recursiveSum(l, start) + recursiveSum(l, start + 1)
        res.append(l(start))

    return recursiveSum(l, 0)


def recursiveSumTupple(orig, l):
    memo = list()
    for i in range(len(l)):
        (el1, el2) = l[i]
        sumEl = sum(l[i])
        # memo[i] = sumEl
        remaining = orig - list(l[i])
        # recursiveSumTupple(remaining, memo)


def bestMerge(tuples):
    acc = 0
    for sublist in tuples:
        minSum = min([pair[0] + pair[1] for pair in sublist])
        acc += minSum
    return acc


def createCustomTuppleList(l):
    result = []
    for idx in range(len(l) - 1):
        op = []
        el = l[idx]
        for idx2 in range(idx + 1, len(l)):
            op.append((el, l[idx2]))
        result.append(op)
    return result


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
        if s >= target:
            return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


if __name__ == "__main__":
    # hanoi(4, "A", "B", "C")

    # print(recursiveSum([10, 89, 4]))
    array = [100, 250, 1000]
    comb = createCustomTuppleList(array)
    print(createCustomTuppleList([100, 250, 1000, 2000 ,3000]))
    print(comb)
    print(bestMerge(comb))
    # recursiveSumTupple(array, comb)
    # subset_sum([3, 9, 8, 4, 5, 7, 10], 15)
