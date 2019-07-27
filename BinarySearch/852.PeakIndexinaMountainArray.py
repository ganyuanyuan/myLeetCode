class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start, end = 0, len(A)
        while start+1< end:
            mid = (start+end)//2
            if mid+1<len(A) and A[mid]<= A[mid+1]:
                start = mid + 1
            else:
                end = mid

        return start if A[start]>A[end] else end

##############################################
#
#        XXX000 type binary search
#
##############################################
