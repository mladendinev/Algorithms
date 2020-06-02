from data_structures.BinaryTree import Node


def allPossibleFBT(N):
    """
    :type N: int
    :rtype: List[TreeNode]
    """
    N -= 1
    if N == 0:
        return [Node(0)]
    ret = []
    for l in range(1, min(20, N), 2):
        for left in allPossibleFBT(l):
            for right in allPossibleFBT(N - l):
                root = Node(0)
                root.left = left
                root.right = right
                ret += [root]
    return ret
