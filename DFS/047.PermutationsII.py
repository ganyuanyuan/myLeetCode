class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = []
        visited = set()
        self.dfs(nums, 0, visited, [], results)
        return results


    def dfs(self, nums, index, visited,  res, results):
        if index == len(nums):
            results.append(res)
            return

        for i in range(len(nums)):
            if i in visited:
                continue
            if i > 0 and i-1 not in visited and nums[i]==nums[i-1]:
                continue
            visited.add(i)
            self.dfs(nums, index+1, visited, res+[nums[i]], results)
            visited.remove(i)
