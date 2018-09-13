class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        if R==0 or C ==0:
            return None

        maxCircle = max((R-r0),r0,(C-c0),c0)
        ans = [[r0,c0]]
        i = 1
        while i <= maxCircle:
            for j in range(-i+1,i+1):
                if r0+j<R and r0+j>=0 and c0+i >=0 and c0+i<C:
                    ans.append([r0+j,c0+i])
            for j in range(i-1,-i-1,-1):
                if r0+i<R and r0+i >= 0 and c0+j<C and c0+j>=0:
                    ans.append([r0+i,c0+j])
            for j in range(i-1,-i-1,-1):
                if r0+j<R and r0+j>=0 and c0-i >=0 and c0-i<C:
                    ans.append([r0+j,c0-i])
            for j in range(-i+1,i+1):
                if r0-i<R and r0-i >= 0 and c0+j<C and c0+j>=0:
                    ans.append([r0-i,c0+j])
            i +=1
        return ans
