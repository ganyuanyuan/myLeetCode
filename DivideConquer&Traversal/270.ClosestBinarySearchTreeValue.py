# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        lower_bound = self.find_lower_bound(root, target)
        upper_bound = self.find_upper_bound(root, target)

        if lower_bound and upper_bound:
            if target-lower_bound.val < upper_bound.val-target:
                return lower_bound.val
            return upper_bound.val
        elif lower_bound:
            return lower_bound.val
        else:
            return upper_bound.val


##############find the biggest node smaller (or equel) than target
    def find_lower_bound(self, root, target):
        if not root:
            return None
        if root.val > target:
            return self.find_lower_bound(root.left, target)
        right = self.find_lower_bound(root.right, target)
        if right:
            return right
        return root

##############find the smallest node bigger (or equel) than target
    def find_upper_bound(self, root, target):
        if not root:
            return None
        if root.val < target:
            return self.find_upper_bound(root.right, target)
        left = self.find_upper_bound(root.left, target)
        if left:
            return left
        return root

#############################################################################
#
#     Another solution is in_order_traverse.
#
##############################################################################
