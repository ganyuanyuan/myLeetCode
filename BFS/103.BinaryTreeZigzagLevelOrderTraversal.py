# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
            
        queue = [root]
        ans = []
        isOddLeverl = True 
        while queue:
            nextQueue = []
            res = []
            for node in queue:
                res.append(node.val)
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            if not isOddLeverl:
                res.reverse()
            ans.append(res)
            queue = nextQueue
            isOddLeverl = not isOddLeverl
            
        return ans  
