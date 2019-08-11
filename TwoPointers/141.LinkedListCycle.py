# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False
        slow, fast = head, head
        while True:
            if fast.next is None:
                break
            fast = fast.next.next
            slow = slow.next
            if not fast or not slow:
                break
            if fast == slow:
                return True
        return False 
