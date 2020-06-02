from data_structures.ListNode import ListNode


def reverseList(head, acc):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if (head.next is None or head is None):
        return head

    result = reverseList(head.next, acc)
    head.next.next = head
    head.next = None

    return result

if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    result2 = reverseList(node, None)

