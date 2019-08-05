# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.leftCount , self.rightCount, self.rootCount = 0,0,0
        self.countNodes(root,x)
        return max(self.leftCount, self.rightCount, n-self.rootCount) > n//2



    def countNodes(self, root,x):
        if not root:
            return 0
        left = self.countNodes(root.left,x)
        right = self.countNodes(root.right,x)
        if root.val == x:
            self.leftCount = left
            self.rightCount = right
            self.rootCount = left+right+1
        return left+right +1
