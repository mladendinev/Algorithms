def canJump(nums):
    return canJumpFromPosition(0, nums)


def canJumpFromPosition(position, nums):
    if position == len(nums) - 1:
        return True

    furthest = min(position + nums[position], len(nums) - 1)

    for next_pos in reversed(range(position + 1, furthest + 1)):
        if canJumpFromPosition(next_pos, nums):
            return True

    return False


x = [2, 3, 1, 1, 4]


def canJumpFromPositionDP(pos, nums, mem):
    if (mem[pos] != "unknown"):
        return True if mem[pos] == "g" else False

    furthest = min(pos + nums[pos], len(nums) - 1) + 1

    for next_pos in range(pos + 1, furthest):
        if canJumpFromPositionDP(next_pos, nums, mem):
            mem[pos] = "g"
            return True
    mem[pos] = "b"
    return False


def can_jump_dp_top_down(nums):
    memo = ["unknown"] * len(nums)
    memo[-1] = "g"
    return canJumpFromPositionDP(0, nums, memo)


def can_jump_dp_bottom_up(nums):
    memo = ["unknown"] * len(nums)
    memo[-1] = "g"

    for i in reversed(range(0, len(nums) - 1)):
        furthest = min(i + nums[i], len(nums) - 1)

        for j in range(i + 1, furthest + 1):
            if memo[j] == "g":
                memo[i] = "g"
                break

    return memo[0] == "g"


print(can_jump_dp_bottom_up(x))
