class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = { i:[] for i in range(n)}
        for i,j in red_edges:
            graph[i].append((j, 1)) #red
        for i,j in blue_edges:
            graph[i].append((j, -1))#blue

        res = [-1 for _ in range(n)]
        res[0] = 0
        queue = [(0, 0)] #node, color
        visited = set([(0, 0)])
        distance = 0
        while queue :
            nextQueue = []
            for node, color in queue:
                if res[node] == -1:
                    res[node] = distance
                for nextNode, newColor in graph[node]:
                    if newColor != color and (nextNode, newColor) not in visited:
                        visited.add((nextNode, newColor) )
                        nextQueue.append((nextNode, newColor) )

            distance += 1
            queue = nextQueue

        return res

##################################################################################
# construct the graph !
#     1. node is (val, color)
#                        |
#                      point in color
#
##################################################################################
