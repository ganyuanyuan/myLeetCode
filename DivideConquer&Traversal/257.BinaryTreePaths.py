# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.results = []
        self.dfs(root, [])
        return ["->".join(result) for result in self.results]


    def dfs(self, node, result):
        if not node:
            return

        if not node.left and not node.right:
            self.results.append(result+[str(node.val)])
            return

        self.dfs(node.left, result+[str(node.val)])
        self.dfs(node.right,result+[str(node.val)])
