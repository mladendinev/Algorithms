def backtrack(l, result, acc):
    acc.append(result)
    for idx, el in enumerate(l):
        result.append(el)
        backtrack(l, result)


def subsets(l):
    acc = []
    backtrack(l, [], acc)


# Second approach with BFS

def permute(nums):
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, acc):
    if not nums:
        acc.append(path)
        # return # backtracking
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1:], path + [nums[i]], acc)


print(permute([1, 2, 3]))
