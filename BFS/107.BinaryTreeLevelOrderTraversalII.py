# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        ans = []
        while queue:
            nextQueue = []
            res = []
            for node in queue:
                res.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right :
                    nextQueue.append(node.right)

            ans.append(res)
            queue = nextQueue
        ans.reverse()
        return ans
