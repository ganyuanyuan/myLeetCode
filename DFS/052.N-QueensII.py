class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.dfs(n, [])
        return self.count

    def dfs(self, n, cols):
        if len(cols) == n:
            self.count += 1
            return
        row = len(cols)
        for col in range(n):
            if self.isValid(cols, row, col):
                self.dfs(n, cols+[col])

    def isValid(self, cols, row, col):
        for r,c in enumerate(cols):
            if c==col or r+c==row+col or r-c==row-col:
                return False
        return True 
