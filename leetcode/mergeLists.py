def merge(nums1, m: int, nums2, n) -> None:
    lastElLeft = m - 1
    lastElRight = n - 1

    k = m + n - 1

    while (lastElLeft >= 0 and lastElRight >= 0):
        if (nums1[lastElLeft] > nums2[lastElRight]):
            nums1[k] = nums1[lastElLeft]
            lastElLeft -= 1

        else:
            nums1[k] = nums2[lastElRight]
            lastElRight -= 1
        k -= 1
    while (lastElRight >= 0):
        nums1[k] = nums2[lastElRight]
        lastElRight -= 1
        k -= 1
    return nums1


def within_range(start, x, end):
    return start <= x <= end


def merge2(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if intervals is None or intervals is [] or len(intervals) == 1:
        return intervals


    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    idx = 1

    prev_start, prev_end = intervals[0]
    while idx <= len(intervals) - 1:
        next_start, next_end = intervals[idx]
        if within_range(prev_start, next_start, prev_end) or within_range(next_start, prev_start, next_end):
            next_start = min(next_start, prev_start)
            next_end = max(prev_end, next_end)
            if (len(result) > 0):
                result[-1] = [next_start, next_end]
            else:
                result.append([next_start, next_end])

        else:
            if [prev_start, prev_end] not in added:
                result.append([prev_start, prev_end])
            result.append([next_start, next_end])
        idx = idx + 1
        prev_start = next_start
        prev_end = next_end

    return result


if __name__ == '__main__':
    # x = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # x =[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    # x = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    x = [[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]

    print(merge2(x))
    # merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
