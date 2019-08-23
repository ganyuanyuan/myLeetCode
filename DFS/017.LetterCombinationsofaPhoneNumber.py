class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        results = []
        self.dfs(digits, 0, '', results, mapping)
        return results


    def dfs(self, digits, index, res, results, mapping):
        if index == len(digits):
            results.append(res)
            return

        for next_char in mapping[digits[index]]:
            self.dfs(digits, index+1, res+next_char, results, mapping)
