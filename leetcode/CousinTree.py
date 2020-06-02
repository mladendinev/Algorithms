# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        if not root:
            return False
        res = self.bfs(root, x, y)
        if res is None:
            return False
        return res[0][0] != res[1][0] and res[0][1] == res[1][1]

        # """
        # :type root: TreeNode
        # :type x: int
        # :type y: int
        # :rtype: bool
        # """

    def bfs(self, root, x, y):
        queue = []

        queue.append((root, 0))
        while (len(queue) > 0):
            el, level = queue.p(0)

            if (el.left is not None):
                if (el.left.val == x or el.left.val == y):
                    x = (el, level + 1)
                queue.append((el.left, level + 1))

            if (el.right is not None):
                if (el.right.val == x or el.right.val == y):
                    x = (el, level + 1)
                queue.append((el.right, level + 1))

            if (x is not None and y is not None):
                return x, y

        return None

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1 = {}
        dict2 = {}
        res = None
        min = 40

        for idx, el in enumerate(list1):
            dict1[el] = idx

        for idx, el in enumerate(list2):
            dict2[el] = idx


        for key, value in dict1.items():
            if dict2.keys().__contains__(key):
                if(abs(dict1[key] - dict2[key]) < min):
                    min = abs(dict1[key] + dict2[key])
                    res = key

        return [res]


