# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return None

        leftLast = self.helper(root.left)
        rightLast = self.helper(root.right)

        if root.left and root.right:
            root.left, root.right,  leftLast.right=  None , root.left ,root.right
            return rightLast
        elif root.left:
            root.left, root.right =  None , root.left
            return leftLast
        elif root.right:
            return rightLast
        else:
            return root
