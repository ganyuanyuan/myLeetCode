class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxArray = [nums[0] for _ in range(len(nums))]
        minArray = [nums[0] for _ in range(len(nums))]


        for i in range(1,len(nums)):
            if nums[i]>=0 :
                maxArray[i] = max(maxArray[i-1]*nums[i], nums[i])
                minArray[i] = min(minArray[i-1]*nums[i], nums[i])
            else:
                maxArray[i] = max(minArray[i-1]*nums[i], nums[i])
                minArray[i] = min(maxArray[i-1]*nums[i], nums[i])
        return max(maxArray)
