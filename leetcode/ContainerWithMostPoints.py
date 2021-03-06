# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate
# (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        max_water = max(max_water, (right - left) * min(height[left], height[right]))
        if height[left] < height[j]:
            left += 1
        else:
            right -= 1
    return max_water


def area(item):
    return item[0] * 2 + item[1] * 2


def minAreaRect(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    sorted(points, key=area)
    return points


print(minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])[0])
