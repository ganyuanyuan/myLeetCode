# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.solution2(root, k)

    def solution1(self, root, k):
        self.bst = []
        self.traverse(root)
        return self.bst[k-1]

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.bst.append(root.val)
        self.traverse(root.right)

#############################################################################
#
#    solution1: simply in-order traverse, return the kth value in array.
#
##############################################################################


    def solution2(self, root, k):
        count = {}
        self.countNodes(root, count)
        return self.quickSelect(root, k, count)


    def countNodes(self, root, count):
        if not root:
            return 0
        left = self.countNodes(root.left, count)
        right = self.countNodes(root.right, count)
        count[root] = left + right + 1
        return left + right +1

    def quickSelect(self, root, k, count):
        if root.left:
            leftCount = count[root.left]
        else:
            leftCount = 0

        if leftCount+1 == k:
            return root.val
        elif leftCount >= k:
            return self.quickSelect(root.left, k, count)
        else:
            return self.quickSelect(root.right, k-leftCount-1, count)



#############################################################################
#
#    solution2:
#         step1: use a hashmap to store the number of each subtree(key:subtree root, value: how many nodes)
#         step2: like quick select:
#                get how many nodes in the left-subtree,
#                discuss in different situations.
#
##############################################################################
