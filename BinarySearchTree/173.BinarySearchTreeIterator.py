# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.stack[-1]
        if top.right:
            node = top.right
            while node :
                self.stack.append(node)
                node = node.left
        else:
            node = self.stack.pop()
            while self.stack and self.stack[-1].right == node:
                node = self.stack.pop()

        return top.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0
#############################################################################
#
#      Non_Recussion version of in_order_traverse
#
##############################################################################
