class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # return self.solution1(nums1, nums2)
        return self.solution2(nums1, nums2)
    
    def solution1(self, nums1, nums2):
        m , n = len(nums1), len(nums2)
        if (m+n)%2 ==1:
            return self.findKth(nums1, nums2, (m+n)//2+1) / 1.0
        else:
            small = self.findKth(nums1, nums2, (m+n)//2)
            big   = self.findKth(nums1, nums2, (m+n)//2+1)
            return (small+big) / 2.0 
        
    def findKth(self, nums1, nums2, k):
        if len(nums1)==0 :
            start, end = nums2[0], nums2[-1]
        elif len(nums2)==0 :
            start, end = nums1[0], nums1[-1]
        else:
            start = min(nums1[0] , nums2[0])
            end   = max(nums1[-1], nums2[-1])
            
        while start+1<end:
            mid = (start+end)//2 
            count1 = self.count(nums1, mid)
            count2 = self.count(nums2, mid)
            if count1+count2 < k:
                start = mid 
            else:
                end = mid 
        
        if self.count(nums1, start) + self.count(nums2, start) >= k:
            return start 
        return end 
    
#    count # small or equal to n
    def count(self, nums, n):
        if not nums:
            return 0
        left, right = 0, len(nums)-1
        while left+1 < right:
            mid = (left+right)//2 
            if nums[mid] <= n:
                left = mid 
            else:
                right = mid 
                
        if nums[right] <= n:
            return right +1 
        elif nums[left] <= n :
            return left +1
        return 0 
   
    def solution2(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if (m+n) %2 ==1:
            return self.findKth2(nums1, 0, nums2, 0 , (m+n)//2+1)/1.0
        else:
            small = self.findKth2(nums1, 0, nums2, 0, (m+n)//2)
            big = self.findKth2(nums1, 0, nums2, 0, (m+n)//2+1)
            return (small+big) /2.0
        
    def findKth2(self, array1, index1, array2, index2, k):
        if index1 == len(array1):
            return array2[index2+k-1]
        if index2 == len(array2):
            return array1[index1+k-1]
        if k==1:
            return min(array1[index1], array2[index2])
        
            
        a = array1[index1+k//2-1] if index1+k//2<=len(array1) else None 
        b = array2[index2+k//2-1] if index2+k//2<=len(array2) else None 
            
        if b is None  or (a is not None and a < b):
            return self.findKth2(array1, index1+k//2, array2, index2, k-k//2)
        else:
            return self.findKth2(array1, index1, array2, index2+k//2, k-k//2)
