class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        visited = set()
        self.dfs(nums, 0, visited, [], results)
        return results

    def dfs(self, nums, index,  visited, res, results):
        if index == len(nums):
            results.append(res)
            return

        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.dfs(nums, index+1, visited, res+[nums[i]], results)
                visited.remove(i)
