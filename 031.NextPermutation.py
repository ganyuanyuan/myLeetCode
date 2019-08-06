class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1]>=nums[i]:
                continue
            for j in range(len(nums)-1, i-1, -1):
                if nums[j]<= nums[i-1]:
                    continue
                nums[i-1], nums[j] = nums[j], nums[i-1]
                left , right = i , len(nums)-1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left +=1
                    right -= 1
                return nums
        nums.reverse()
        return nums
