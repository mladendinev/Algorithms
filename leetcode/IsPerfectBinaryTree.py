class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if (root is None):
            return -1

        left = self.isCompleteTree(root.left)
        right = self.isCompleteTree(root.right)


