class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n > 0:
            if n%26==0:
                ans += 'Z'
                n = n//26 -1
            else:
                ans += chr(n%26 + 64)
                n = n//26
        return ans[::-1]
                
