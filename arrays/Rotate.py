def rotate(nums, k) -> None:
    k = k % len(nums)
    if (len(nums) == 0 or len(nums) == 1 or k == 0):
        return

    lastKelements = nums[-k:]
    firstBeforeElements = nums[:len(nums) - k]
    nums.clear()
    nums.extend(lastKelements)
    nums.extend(firstBeforeElements)


if __name__ == '__main__':
    rotate([1, 2], 2)
