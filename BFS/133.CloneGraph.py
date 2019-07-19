"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        root = node
        nodes = self.getAllNodes(node)
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val, [])

        for node in nodes:
            for neighbor in node.neighbors:
                mapping[node].neighbors.append(mapping[neighbor])

        return mapping[root]



    def getAllNodes(self, node):
        res = set([node])
        queue = [node]
        index = 0
        while index < len(queue):
            top = queue[index]
            for neighbor in top.neighbors:
                if neighbor not in res:
                    queue.append(neighbor)
                    res.add(neighbor)
            index += 1

        return res

##################################################################################
# 3 points:
#     1. bfs get all get nodes
#     2. using hash mapping clone every node
#     3. clone edges.
# 
##################################################################################
