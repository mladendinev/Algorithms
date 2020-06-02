def merge(a, b, lastA, lastB):
    indexA = lastA - 1
    indexB = lastB - 1
    indedMerged = lastA + lastB - 1

    while (indexB >= 0):
        if indexA >= 0 and a[indexA] > b[indexB]:
            a[indedMerged] = a[indexA]
            indexA -= 1
        else:
            a[indedMerged] = b[indexB]
            indexB -= 1
        indedMerged -= 1
    return a


def sortByAnagrams(l):
    def sortChars(s):
        return "".join(sorted(s))

    l.sort(key=lambda x: sortChars(x))
    return l


def knapSack2(W, wt, val, n):
    if (n == 0 or W == 0):
        return 0

    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)

    return max(knapSack2(W, wt, val, n - 1), val[n - 1] + knapSack2(W - wt[n - 1], wt, val, n - 1))


def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        # return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), knapSack(W, wt, val, n - 1))
        return max(knapSack(W, wt, val, n - 1),
                   val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1))

    # end of function knapSack


# To test above function


if __name__ == "__main__":
    a = [20, 30, 50, 60, 70, None, None, None, None]
    b = [10, 20, 32, 35]
    # lastIndex = next(idx for idx, x in enumerate(a) if x is None)
    # print(lastIndex)
    # res = merge(a, b, lastIndex, len(b))
    # print(res)

    strArray1 = ["tap", "evil", "pat", "placebo", "vile", "obecalp"]
    print(sortByAnagrams(strArray1))

    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapSack2(W, wt, val, n))
