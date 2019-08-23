# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        largest = root.val
        ans = 1
        level = 1
        queue = [root]
        while queue:
            level +=1
            next_queue = []
            total = 0
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                    total += node.left.val
                if node.right :
                    next_queue.append(node.right)
                    total += node.right.val
            if total > largest:
                largest = total
                ans = level

            queue = next_queue

        return ans 
