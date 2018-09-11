class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            ans += 26**(len(s)-i-1)*(ord(s[i])-64)

        return ans
