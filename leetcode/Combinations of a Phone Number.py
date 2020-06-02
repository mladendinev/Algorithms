def letterCombinations(digits):
    map = {1: [], 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    """
    :type digits: str
    :rtype: List[str]
    """
    if (len(digits) == 0):
        return []
    if (len(digits) == 1):
        return map[int(digits[0])]

    prev = letterCombinations(digits[:-1])
    permutations = map[int(digits[-1])]
    if not prev:
        return [k for k in permutations]
    else:
        return [s + c for s in prev for c in permutations]


print(letterCombinations("1235"))
