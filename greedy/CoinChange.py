def change(list_coins, target):
    m = [[0 for _ in range(target + 1)] for _ in range(len(list_coins) + 1)]
    for i in range(1, target + 1):
        m[0][i] = float('inf')
    return m


def getWays(change, coins, x, currentChange):
    solution = []
    if (change == 0 or (change > 0 and len(coins) == x)):
        return 0

    if (currentChange < change):
        solution.append(coins[x - 1])

    getWays()
