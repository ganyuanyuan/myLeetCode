class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []
        self.dfs(n, [])
        return self.results

    def dfs(self, n, cols):
        if len(cols)==n:
            self.results.append(self.drawChessBoard(n, cols))
            return

        row = len(cols)
        for col in range(n):
            if self.isValid(cols, row, col):
                self.dfs(n, cols+[col])


    def isValid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col or r+c==row+col or r-c ==row-col:
                return False
        return True


    def drawChessBoard(self, n, cols):
        ans = []
        for col in cols:
            row = ''
            for i in range(n):
                if i==col:
                    row += 'Q'
                else:
                    row += '.'
            ans.append(row)
        return ans

#############################################################################
#
#     use an array called cols to store position:
#            index of array ----> represent ith row   
#
##############################################################################
