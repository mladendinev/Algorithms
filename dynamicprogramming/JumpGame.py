# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


def canJumpFromPosition(position, nums, memo):
    if memo[position] != "x":
        return True if memo[position] == "g" else False

    furthest_jump = min(position + nums[position], len(nums) - 1)

    #   first optimisation // reverse
    # for next in range(position + 1, furthest_jump + 1)[::-1]:

    for next in range(position + 1, furthest_jump + 1):
        if canJumpFromPosition(next, nums, memo):
            memo[position] = "g"
            return True

    memo[position] = "b"
    return False


def canJump(nums):
    cache = {}
    for idx, num in enumerate(nums):
        cache[idx] = "x"

    cache[len(nums) - 1] = "g"

    # for i in reversed(range(0, len(nums) - 2)):
    #     furthest_jump = min(i + nums[i], len(nums) - 1)

    #     for j in range(i + 1, furthest_jump + 1):
    #         if cache[j] == "g":
    #             cache[i] = "g"
    #             break
    #
    # return cache[0] == "g"
    return canJumpFromPosition(0, nums, cache)


print(canJump([3, 2, 1, 0, 4]))



