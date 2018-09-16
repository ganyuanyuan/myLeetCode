class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m ==0 or n==0:
            return 0
        line = [1]*n
        matrix = [line]*m

        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] =matrix[i-1][j]+ matrix[i][j-1]

        return matrix[-1][-1]
