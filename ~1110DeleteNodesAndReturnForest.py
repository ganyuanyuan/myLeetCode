# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        toDeleteSet = set(to_delete)
        ans = []
        self.helper(root, True, ans , toDeleteSet)

        return ans

    def helper(self, root, isRoot, ans, toDeleteSet):
        if not root:
            return None

        isDeleteRoot = root.val in toDeleteSet
        if not isDeleteRoot and isRoot:
            ans.append(root)

        root.left = self.helper(root.left, isDeleteRoot, ans, toDeleteSet)
        root.right = self.helper(root.right, isDeleteRoot, ans, toDeleteSet)

        if isDeleteRoot :
            return None
        return root


###########################################
# recursion!!
# if a node is root but not deleted, put it in the answer
###########################################
