class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] , nums[fast] = nums[fast], nums[slow]
                slow +=1
            fast +=1

        return nums
