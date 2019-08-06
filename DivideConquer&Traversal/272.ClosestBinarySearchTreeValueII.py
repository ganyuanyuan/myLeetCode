# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        upper_stack = self.get_stack(root, target)
        lower_stack = list(upper_stack)

        if lower_stack[-1].val > target:
            self.move_lower(lower_stack)
        else:
            self.move_upper(upper_stack)

        res = []
        for _ in range(k):
            if self.is_left_closer(lower_stack, upper_stack, target):
                res.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                res.append(upper_stack[-1].val)
                self.move_upper(upper_stack)

        return res

    def is_left_closer(self, lower_stack, upper_stack, target):
        if not lower_stack:
            return False
        if not upper_stack:
            return True
        return target-lower_stack[-1].val < upper_stack[-1].val - target

    def move_upper(self, stack):
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()

    def move_lower(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()


    def get_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return stack
#############################################################################
#
#      Best solution !  TIME:O(k+log(n))  SPACE: O(log(n))
#      Non_Recussion_Iterator :
#          1. use two stacks to store the path
#          2. upper --> move_upper  & lower --> move_lower
#
##############################################################################

    def solution1(self, root, target):
        self.bst = []
        self.traverse(root)

        pivot, distance = 0 , abs(target-self.bst[0])
        for i, num in enumerate(self.bst):
            if abs(num-target)< distance:
                pivot = i
                distance = abs(num-target)

        left, right = pivot , pivot+1
        res = []
        for _ in range(k):
            if self.isLeftCloser(left, right, target):
                res.append(self.bst[left])
                left -= 1
            else:
                res.append(self.bst[right])
                right += 1
        return res

    def isLeftCloser(self, left, right, target):
        if left< 0:
            return False
        if right >= len(self.bst):
            return True
        return abs(target-self.bst[left]) < abs(target-self.bst[right])



    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.bst.append(root.val)
        self.traverse(root.right)

#############################################################################
#
#      1. in_order_traverse
#      2. find closest value
#      3. two pointers
#
#       TIME: O(n)
#
##############################################################################
