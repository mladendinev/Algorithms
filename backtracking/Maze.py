maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 0]]


def printSol(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")


def isItValid(x, y):
    if x >= 0 and x < len(maze) and y >= 0 and y < len(maze) and maze[x][y] == 1:
        return True
    return False

d


def solve():
    # sol = [[0 for j in range(4)] for i in range(4)]
    # maze = [[0, 0, 0, 0],
    #         [0, 1, 0, 1],
    #         [0, 1, 0, 0],
    #         [1, 1, 1, 1]]
    def solveMaze(x, y, sol):
        if x == len(maze) - 1 and y == len(maze) - 1 and maze[x][y] == 1:
            sol[x][y] = 1
            return True

        if isItValid(x, y) == True:
            sol[x][y] = 1

            # Move forward in x
            if solveMaze(x + 1, y, sol) == True:
                return True

            # Move forward in y
            if solveMaze(x, y + 1, sol) == True:
                return True

            sol[x][y] = 0
            return False



    sol = [[0 for _ in range(len(maze))] for _ in range(len(maze))]
    if not solveMaze(0, 0, sol):
        print("Solution doesn't exist")
        return False
    printSol(sol)
    return True

solve()
