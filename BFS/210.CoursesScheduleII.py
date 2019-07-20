class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses ==0 :
            return []

        indegrees, postCourses = self.helper(numCourses, prerequisites)

        queue = []
        for n in range(numCourses):
            if indegrees[n] == 0:
                queue.append(n)

        index = 0
        while index< len(queue):
            top = queue[index]
            for post in postCourses[top]:
                indegrees[post] -= 1
                if indegrees[post] == 0:
                    queue.append(post)

            index += 1

        if len(queue) == numCourses:
            return queue
        return []




    def helper(self, n, pres):
        indegrees, postCourses = {}, {}
        for i in range(n):
            indegrees[i] = 0
            postCourses[i] = []
        for pre in pres:
            indegrees[pre[0]] += 1
            postCourses[pre[1]].append(pre[0])

        return indegrees, postCourses

##################################################################################
# Topological Sorting
#     1. find indegrees first
#     2. bfs traverse
#
##################################################################################
