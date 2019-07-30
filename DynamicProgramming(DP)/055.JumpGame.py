class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        final = 0
        for i in range(len(nums)):
            if i > final:
                return False
            final = max(final, i+nums[i])

        return final >= len(nums)-1

#############################################################################
#
#     this is greedy , not dp !!
#     dp can solve this problem ----> time O(n**2)
#     greedy                    ----> time O(n)
#
##############################################################################
