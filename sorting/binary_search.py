def binary_search(n, target):
    N = len(n)
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if n[mid] == target:
            return mid
        elif n[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def searchRange(nums, target):
    N = len(nums)
    l, r = 0, N - 1
    while l <= r:
        mid = (l + r) / 2
        if nums[mid] == target:
            break
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    if l > r: return [-1, -1]

    l = r = mid
    while l > 0:
        if nums[l - 1] == target:
            l -= 1
        else:
            break
    while r < N - 1:
        if nums[r + 1] == target:
            r += 1
        else:
            break

    return [l, r]
