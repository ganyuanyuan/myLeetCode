class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setn = set(nums)
        for i in range(len(nums)+1):
            if i not in setn:
                return i
