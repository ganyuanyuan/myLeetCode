# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #solution1
        #ans , _, _ = self.helper(root)
        #return ans

        self.isValid = True
        self.value = None
        self.traversal(root)
        return self.isValid

    def traversal(self, root):
        if not root:
            return
        self.traversal(root.left)
        if self.value is not None and self.value>= root.val:
            self.isValid = False
            return
        self.value = root.val
        self.traversal(root.right)



    def helper(self, root):
        if not root:
            return True, None, None

        isLeft, leftSmall, leftLarge = self.helper(root.left)
        isRight, rightSmall, rightLarge = self.helper(root.right)

        if not isLeft or not isRight:
            return False, None, None

        if not leftLarge and not rightSmall:
            return True, root.val, root.val
        elif not leftLarge:
            return root.val < rightSmall, root.val, rightLarge
        elif not rightSmall:
            return leftLarge< root.val, leftSmall, root.val
        else:
            return leftLarge< root.val< rightSmall, leftSmall, rightLarge



##############################################
#
#     solution1 : divide and conquer
#
#     solution2 :traverse
#
##############################################
