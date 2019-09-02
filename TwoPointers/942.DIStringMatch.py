class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        return self.solution2(S)

    def solution2(self, S):
        left, right = 0, 0
        ans = [0]
        for char in S:
            if char == "I":
                right +=1
                ans.append(right)
            else:
                left -=1
                ans.append(left)
        return [num-left for num in ans]




    def solution1(self, S):
        n = len(S)+1
        ans = [i for i in range(n)]
        left = 0
        while left<len(S):
            if S[left] == "D":
                right = left +1
                while right<len(S) and S[right] == "D":
                    right +=1
                self.reverse(left, right, ans)
                left = right
            left += 1

        return ans

    def reverse(self, left, right, ans):
        while left < right:
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
