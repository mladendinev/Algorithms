# Given a 2d grid map of '1's (land) and '0's (water),
# count the number of islands.
# An island is surrounded by water
# and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

def number_of_islands(grid):
    visited = set()
    counter = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "1" and not (row, column) in visited:
                counter += 1
                bfs((row, column), grid, visited)
    return counter


def in_range(start, x, end):
    if start <= x <= end:
        return True


def bfs(x, grid, visited):
    stack = []

    stack.append(x)
    while stack:
        el = stack.pop()
        if not el in visited:
            visited.add(el)

            if in_range(0, el[0] + 1, len(grid) - 1) and grid[el[0] + 1][el[1]] == "1":
                stack.append((el[0] + 1, el[1]))

            if in_range(0, el[1] + 1, len(grid[0]) - 1) and grid[el[0]][el[1] + 1] == "1":
                stack.append((el[0], el[1] + 1))

            if in_range(0, el[1] - 1, len(grid[0]) - 1) and grid[el[0]][el[1] - 1] == "1":
                stack.append((el[0], el[1] - 1))

            if in_range(0, el[0] - 1, len(grid) - 1) and grid[el[0] - 1][el[1]] == "1":
                stack.append((el[0] - 1, el[1]))


a = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(number_of_islands(a))
