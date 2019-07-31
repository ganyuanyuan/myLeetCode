class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.dfs(candidates, 0, [], 0, target)

        return self.ans

    def dfs(self, candidates, index, temp,  total, target):
        if total == target:
            self.ans.append(temp)
            return

        for i in range(index, len(candidates)):
            if total + candidates[i] > target:
                break
            self.dfs(candidates, i, temp+[candidates[i]], total+candidates[i], target)
