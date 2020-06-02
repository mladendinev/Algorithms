class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.left = left
        self.right = right
        self.val = val
        self.next = next


class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, val):
        return self.insertNode(val, self.root)

    def insertNode(self, val, node):
        if node is None:
            node = Node(val)
            return node

        if (val > node.val):
            node.right = self.insertNode(val, node.right)
        else:
            node.left = self.insertNode(val, node.left)
        #
        return node

    def bst(self):
        return self.bstToGst(self.root)

    def bstToGst(self, root, acc):
        if root.right:
            self.bstToGst(root.right)
        acc += root.val
        root.val = self.val = self.val + root.val
        if root.left:
            self.bstToGst(root.left)
        return root

    def levelOrder(self):
        queue = []
        result = []
        temp = []
        lastLevel = 0
        queue.append((self.root, 1))
        while (len(queue) > 0):
            node, level = queue.pop(0)

            if (lastLevel != level):
                result.append(temp)
                temp = []
                lastLevel = level

            if node.left is not None:
                queue.append((node.left, level + 1))
                temp.append(node.left.val)
            if node.right is not None:
                queue.append((node.right, level + 1))
                temp.append(node.right.val)
        return result

    def connect(self):
        self.connectRec(self.root)
        return self.root

    def connectRec(self, root):
        start = root
        while (start is not None):
            cur = start
            while (cur is not None):
                if cur.left is not None:
                    cur.left.next = cur.right
                if cur.right is not None and cur.next is not None:
                    cur.right.next = cur.next.left

                cur = cur.next
            start = start.left

    def isBinaryTree(self):
        x = [1]

        def isBinaryTreeRec2(root):
            if root is None:
                return True

            if not isBinaryTreeRec2(root.left):
                return False

            if x[0] >= root.val:
                return False
            x[0] = root.val
            if not isBinaryTreeRec2(root.right):
                return False
            return True

        def isBinaryTreeMinMax(root, min, max):
            if root is None:
                return True

            if min is not None and root.val <= min or max is not None and root.val > max:
                return False
            if not isBinaryTreeMinMax(root.left, min, root.val) or not isBinaryTreeMinMax(root.right,
                                                                                          root.val,
                                                                                          max):
                return False

        return isBinaryTreeMinMax(self.root, None, None)


if __name__ == '__main__':
    node = Node(5)
    node.left = Node(1)
    node.right = Node(4)
    node.right.left = Node(3)
    node.right.right = Node(6)
    tree = Tree(node)
    # print(tree.isBinaryTree())
    import numpy

    expected = [["sol"], ["wow"], ["gap"], ["hem"], ["yap"], ["bum"], ["ugh", "ugh"], ["aha"], ["jab"], ["eve"],
                ["bop"],
                ["lyx"], ["jed"], ["iva"], ["rod"], ["boo"], ["brr"], ["hog"], ["nay"], ["mir"], ["deb", "deb"],
                ["aft"],
                ["dis"], ["yea"], ["hos"], ["rye"], ["hey"], ["doc"], ["bob"], ["eel"], ["pen"], ["job"], ["max"],
                ["oho"],
                ["lye"], ["ram"], ["nap"], ["elf"], ["qua"], ["pup", "pup"], ["let"], ["gym"], ["nam"], ["bye"],
                ["lon"]]

    actual = [["hos"], ["boo", "bob"], ["nay"], ["deb", "deb"], ["wow"], ["bop"], ["brr"], ["hey"], ["rye"], ["eve"],
              ["elf"], ["pup", "pup"], ["bum"], ["iva"], ["lyx"], ["yap"], ["ugh", "ugh"], ["hem"], ["rod"], ["aha"],
              ["nam"], ["gap"], ["yea"], ["doc"], ["pen"], ["job"], ["dis"], ["max"], ["oho"], ["jed"], ["lye"],
              ["ram"], ["qua"], ["mir"], ["nap"], ["hog"], ["let"], ["gym"], ["bye"], ["lon"], ["aft"], ["eel"],
              ["sol"], ["jab"]]
    import collections

    print(collections.Counter("bob"))
    print(collections.Counter("boo"))
    print(hash(frozenset(collections.Counter("bob"))))
    print(hash(frozenset(collections.Counter("boo"))))
    print(expected)
