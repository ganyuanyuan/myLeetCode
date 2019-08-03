# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        pointer = dummy
        flag = 0
        while l1 or l2:
            if l1 and l2:
                num = l1.val + l2.val
            elif l1:
                num = l1.val
            else:
                num = l2.val
            node = ListNode((num+flag)%10)
            flag = (num+flag)//10
            pointer.next = node
            pointer = node
            if l1 :
                l1 = l1.next
            if l2:
                l2 = l2.next


        if flag==1:
            pointer.next = ListNode(1)

        return dummy.next 
