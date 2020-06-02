from data_structures.Trie import Trie


class Solution(object):
    def within_range(self, start, x, end):
        if start <= x <= end:
            return True

    def check_bucket(self, bucket, hash_list, res):
        hash_code = hash(frozenset(bucket))
        if hash_code in hash_list:
            res.append(hash_list[hash_code])

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        unique_chars = {}
        list_hashes = {}
        for word in words:
            unique_chars
        list_hashes = {hash(frozenset(list(x))): x for x in words}

        if not board or not words:
            return []

        rows = len(board) - 1
        columns = len(board[0]) - 1
        visited = set()
        x = 0
        y = 0
        result = []
        to_be_visited = [(x, y)]
        while to_be_visited:
            x, y = to_be_visited.pop()
            visited.add((x, y))
            char = board[x][y]
            print(char)
            bucket = [char]

            if self.within_range(0, x + 1, rows):
                nextX = board[x + 1][y]
                bucket.append(nextX)
                self.check_bucket(bucket, list_hashes, result)
                if not (x + 1, y) in visited:
                    to_be_visited.append((x + 1, y))

            if self.within_range(0, y + 1, columns):
                nextY = board[x][y + 1]
                bucket.append(nextY)
                self.check_bucket(bucket, list_hashes, result)

                if not (x, y + 1) in visited:
                    to_be_visited.append((x, y + 1))

            if self.within_range(0, x - 1, rows):
                prevX = board[x - 1][y]
                bucket.append(prevX)
                self.check_bucket(bucket, list_hashes, result)

                if not (x - 1, y) in visited:
                    to_be_visited.append((x - 1, y))

            if self.within_range(0, y - 1, columns):
                prevY = board[x][y - 1]
                bucket.append(prevY)
                self.check_bucket(bucket, list_hashes, result)

                if not (x, y - 1) in visited:
                    to_be_visited.append((x, y - 1))

        return result

    def buildTree(self, words):
        trie = Trie()

        for word in words:
            trie.insert(word)

        return trie.root

    def findWords2(self, board, words):
        trie = self.buildTree(words)
        result = set()
        for row in range(len(board)):
            for column in range(len(board[0])):
                self.dfs(board, row, column, trie, "", result)
        return result

    def dfs(self, board2, row, column, trie, path, res):
        if trie.terminating:
            res.add(path)
            trie.terminating = True
        if row < 0 or row >= len(board2) or column < 0 or column >= len(board2[0]):
            return
        tmp = board2[row][column]
        trie = trie.children.get(tmp)
        if not trie:
            return
        board2[row][column] = "#"
        self.dfs(board2, row + 1, column, trie, path + tmp, res)
        self.dfs(board2, row - 1, column, trie, path + tmp, res)
        self.dfs(board2, row, column - 1, trie, path + tmp, res)
        self.dfs(board2, row, column + 1, trie, path + tmp, res)
        board2[row][column] = tmp


if __name__ == '__main__':
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    word = ["oath", "pea", "eat", "rain"]
    print(Solution().findWords2(board, word))
