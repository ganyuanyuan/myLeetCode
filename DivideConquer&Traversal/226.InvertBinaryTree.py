# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root :
            return None

        leftChild = self.invertTree(root.left)
        rightChild = self.invertTree(root.right)
        root.left = rightChild
        root.right = leftChild

        return root 
