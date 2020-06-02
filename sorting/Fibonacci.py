def fib(n):
    memo = {}

    def fib(n, memo):
        if (n == 0 or n == 1):
            return n

        if n not in memo:
            memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

        return memo

    fib(n, memo)


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


# fib(3)


def fibRec(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibRec(n - 1) + fibRec(n - 2)


fib1 = memoize(fibRec)
print(fib1(7))
