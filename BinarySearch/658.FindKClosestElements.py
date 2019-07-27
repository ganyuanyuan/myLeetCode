class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []

        start, end = 0, len(arr)-1
        while start+1< end:
            mid = (start+end) // 2
            if arr[mid] >= x :
                end = mid
            else:
                start = mid
        if self.leftIsClose(arr, start, end, x):
            index = start
        else:
            index = end

        left, right = index-1, index+1
        for _ in range(k-1):
            if self.leftIsClose(arr, left, right, x):
                left -= 1
            else:
                right +=1

        return arr[left+1:right]




    def leftIsClose(self, arr, left, right, x):
        if right>=len(arr):
            return True
        if left<0:
            return False
        return x-arr[left]<= arr[right]-x
