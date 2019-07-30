class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0 , len(s)-1
        while left<right:
            if s[left] != s[right]:
                return self.isValid(s[left+1:right+1]) or self.isValid(s[left:right])
            left += 1
            right -= 1
        return True

    def isValid(self, s):
        return s == s[::-1]
