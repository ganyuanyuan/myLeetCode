class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.results = []
        self.dfs(s,  [])
        return self.results

    def dfs(self, s,  result):
        if len(s) ==0:
            self.results.append(result)
            return

        for i in range(len(s)):
            if self.isPali(s[:i+1]):
                self.dfs(s[i+1:],  result + [s[:i+1]])


    def isPali(self, s):
        return s[::-1] == s
