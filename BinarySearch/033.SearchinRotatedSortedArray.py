class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums :
            return -1
        return solution1(nums, target)

    def solution1(self, nums, target):
        if len(nums)==1:
            if nums[0] == target:
                return 0
            return -1

        mid = len(nums)//2
        left = self.solution1(nums[:mid], target)
        right = self.solution1(nums[mid:], target)
        if left != -1:
            return left
        elif right != -1:
            return mid + right
        else:
            return -1

#############################################################################
#
#      solution1: divided nums to 2 parts
#
##############################################################################

    def solution2(self, nums, target):
        start ,end = 0, len(nums)-1
        while start +1 < end:
            mid = (start+end)//2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        if nums[start]< nums[end]:
            pivot = start
        else:
            pivot = end

        left , right = 0, len(nums)-1
        while left +1 < right :
            mid = (left+right)//2
            if nums[mid+pivot-len(nums)]== target:
                return (mid+pivot)%len(nums)
            elif nums[mid+pivot-len(nums)]< target:
                left = mid
            else:
                right = mid

        if nums[left+pivot-len(nums)]== target:
            return (left+pivot)%len(nums)
        if nums[right+pivot-len(nums)]== target:
            return (right+pivot)%len(nums)
        return -1


#############################################################################
#
#    solution2: twice binary search
#         first----> find pivot
#         second---> find target
#
##############################################################################
