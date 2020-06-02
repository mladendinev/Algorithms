class Solution(object):
    def nextGreatestLetter(self, letters, target):
        n = len(letters)
        low, hi = 0, n

        while (low < hi):
            mid = low + (hi - low) / 2
            if (letters[mid] > target):
                hi = mid
            else:
                low = mid + 1
        return letters[low % n]
