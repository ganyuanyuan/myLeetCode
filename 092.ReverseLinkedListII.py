# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre1, p1 = None, head
        for _ in range(m-1):
            pre1 = p1
            p1 = p1.next

        pre2, p2 = pre1, p1
        for _ in range(n-m+1):
            pre2 = p2
            p2 = p2.next

        pre , curr = None , p1
        while pre != pre2:
            next = curr.next
            curr.next = pre
            pre , curr = curr, next

        if pre1 is None :
            head = pre
        else:
            pre1.next = pre
        p1.next = p2
        return head

##################################################################################
#  step1 ----> split linked list in 3 pieces
#
#  step2 ----> reverse the middle part                                   
#
##################################################################################
