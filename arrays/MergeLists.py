from data_structures.ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    Solution().mergeTwoLists(node1, node4)
