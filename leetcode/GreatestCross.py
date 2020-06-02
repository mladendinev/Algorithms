class Entry:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def inverse(rows, columns, matrix):
    res = list()
    for column in range(columns):
        bulider = ''
        for row in range(rows):
            bulider += matrix[row][column]
        res.append(bulider)
    return res


def findPairsRows(idx, el):
    current_index = 0
    pairs = list()
    while current_index < len(el):
        if el[current_index] == 'G':
            start = current_index
            end = current_index
            pairs.append(((idx, start), (idx, midpoint(start, end)), (idx, end)))
            while end < len(el):
                if end + 1 < len(el) and el[end + 1] == 'G':
                    end += 1
                    if end != start and ((end - start) % 2) == 0:
                        pairs.append(((idx, start), (idx, midpoint(start, end)), (idx, end)))
                else:
                    break
        current_index += 1
    return pairs


def findPairsColumns(idx, el):
    current_index = 0
    pairs = list()
    while current_index < len(el):
        if el[current_index] == 'G':
            start = current_index
            end = current_index
            pairs.append(((start, idx), (midpoint(start, end), idx), (end, idx)))
            while end < len(el):
                if end + 1 < len(el) and el[end + 1] == 'G':
                    end += 1
                    if end != start and ((end - start) % 2) == 0:
                        pairs.append(((start, idx), (midpoint(start, end), idx), (end, idx)))
                else:
                    break
        current_index += 1
    return pairs


def midpoint(x, y):
    if x != y:
        return int((x + y) / 2)
    else:
        return y


def findBestScores(results):
    if (len(results) == 0):
        return 0
    maxProduct = results[0]["score"]
    # results_iter = iter(results)
    for idx, element in enumerate(results):
        # get the next item
        score = element["score"]
        currStartRow, currEndRow, currStartCol, currEndCol = element["cross"]
        idx += 1
        for nextElement in results[idx:]:
            interescted = False
            nextStartRow, nextEndRow, nextStartCol, nextEndCol = nextElement["cross"]
            nextElementScore = nextElement["score"]

            # on the same row
            if currStartRow[0] == nextStartRow[0]:
                if (len(set(range(currStartRow[1], currEndRow[1])).intersection(
                        set(range(nextStartRow[1], nextStartRow[1])))) > 0):
                    interescted = True

            # on the sam column
            if currStartCol[1] == nextStartCol[1]:
                if (len(set(range(currStartCol[0], currEndRow[0])).intersection(
                        set(range(nextStartRow[0], nextStartRow[0])))) > 0):
                    interescted = True

            # intersect row with column
            if (set(range(currStartRow[1], currEndRow[1] + 1))).__contains__(nextStartCol[1]):
                if (set(range(nextStartCol[0], nextEndCol[0] + 1))).__contains__(currStartRow[0]):
                    interescted = True

            if (set(range(nextStartRow[1], nextEndRow[1] + 1))).__contains__(currStartCol[1]):
                if (set(range(currStartCol[0], currEndCol[0] + 1))).__contains__(nextStartRow[0]):
                    interescted = True

            if interescted is False:
                newscore = nextElementScore * score
                if newscore > maxProduct:
                    maxProduct = newscore
                # break
    return maxProduct


def interesction(rows, columns):
    scores = list()
    for row in rows:
        for (startRow, midRow, endRow) in row:
            for col in columns:
                for (startCol, midCol, endCol) in col:
                    difRow = (endRow[1] - startRow[1])
                    difCol = (endCol[0] - startCol[0])
                    if midRow == midCol and difRow == difCol and endRow and endRow != endCol and startRow != startCol:
                        score = (difRow + 1) * 2 - 1

                        scores.append({"cross": (startRow, endRow, startCol, endCol), "score": score})
    return scores


from functools import reduce

if __name__ == "__main__":
    # matrix = ["GGGGGG", "GBBBGB", "GGGGGG", "GGBBGB", "GGGGGG"]
    matrix = ["GGGGGGGGGG", "GBBBBBBGGG", "GGGGGGGGGG", "GGGGGGGGGG", "GBBBBBBGGG", "GGGGGGGGGG", "GBBBBBBGGG",
              "GBBBBBBGGG", "GGGGGGGGGG"]
    # matrix = ["BBGGBGGBBGGGB",
    #           "BBGGBGGBBGGGB",
    #           "BBGGBGGBBGGGB",
    #           "BBGGBGGBBGGGB",
    #           "GGGGGGGGGGGGG",
    #           "BBGGBGGBBGGGB",
    #           "GGGGGGGGGGGGG",
    #           "BBGGBGGBBGGGB",
    #           "BBGGBGGBBGGGB",
    #           "GGGGGGGGGGGGG",
    #           "GGGGGGGGGGGGG",
    #           "GGGGGGGGGGGGG",
    #           "BBGGBGGBBGGGB",
    #           "GGGGGGGGGGGGG"]
    columns = inverse(len(matrix), len(matrix[0]), matrix)
    res = interesction([findPairsRows(idx, el) for idx, el in enumerate(matrix)],
                       [findPairsColumns(idx, el) for idx, el in enumerate(columns)])
    print(res)
    newlist = sorted(res, key=lambda k: k['score'], reverse=True)
    print(newlist)
    print([el["score"] for el in newlist])
    findBestScores(newlist)
    # assert reduce(lambda x, y: x * y, kur[:2]) == 289
    # for idx, el in enumerate(matrix):
    #     print("ROW", idx)
    #     print("RESULTS", findPairsRows(idx, el))
    #     print('\n')
    #
    # for idx, el in enumerate(columns):
    #     print("COLUMNS", idx)
    #     print("RESULTS", findPairsColumns(idx, el))
    #     print('\n')
# print("COLUMNS {}".format([findPairsRows(el) for el in columns]))
