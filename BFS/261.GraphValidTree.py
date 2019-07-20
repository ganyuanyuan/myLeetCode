class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != (len(edges)+1):
            return False

        return self.solution1(n, edges)


    def solution1(self, n, edges):
        neighbors = { i:[] for i in range(n)}

        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        queue = [0]
        visited = set([0])
        index = 0
        while index < len(queue):
            top = queue[index]
            for neighbor in neighbors[top]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            index +=1

        return len(queue) == n

##################################################################################
# solution 1 ---->bfs traverse
#
##################################################################################



    def solution2(self, n, edges):
        self.father = {i: i  for i in range(n)}
        self.size = n

        for x,y in edges:
            self.union(x, y)
        return self.size == 1

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.size -= 1
            self.father[rootA] = rootB

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for a in path:
            self.father[a] = node

        return node

##################################################################################
# solution 2 ---->union find :
#        1. hash ---->father
#        2. union
#        3. find 
#
##################################################################################
