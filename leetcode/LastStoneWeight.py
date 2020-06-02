import heapq

class Solution:
    def lastStoneWeight(self, A):
        h = [-x for x in A]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]

if __name__ == '__main__':
    k = [2, 7, 4, 1, 8, 1]
    Solution().lastStoneWeight(k)