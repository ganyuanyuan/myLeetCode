import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        return self.solution3(arrays)
        
    
    
    #solution1: heapq   
    def solution1(self, arrays):
        if not arrays:
            return []
            
        ans = []
        heap = []
        for i in range(len(arrays)):
            if arrays[i]:
                heapq.heappush(heap, (arrays[i][0], i, 0))
                
        while heap:
            top, i, index= heapq.heappop(heap)
            ans.append(top)
            if index+1<len(arrays[i]):
                heapq.heappush(heap, (arrays[i][index+1], i , index+1))
                
        return ans 
    
    #like merge sort: divide arrays to two parts, from up to down
    def solution2(self, arrays):
        if not arrays:
            return []
        return self.mergeArrays(arrays, 0, len(arrays)-1)
        
    def mergeArrays(self, arrays, start, end):
        if start==end:
            return arrays[start]
            
        mid = (start+end)//2 
        left = self.mergeArrays(arrays, start, mid)
        right = self.mergeArrays(arrays, mid+1, end)
        return self.mergeTwoArrays(left, right)
        
    def mergeTwoArrays(self, array1, array2):
        i,j = 0,0 
        newArray = []
        while i<len(array1) and j < len(array2):
            if array1[i]<= array2[j]:
                newArray.append(array1[i])
                i += 1 
            else:
                newArray.append(array2[j])
                j += 1 
        while i<len(array1):
            newArray.append(array1[i])
            i += 1 
        while j< len(array2):
            newArray.append(array2[j])
            j += 1 
            
        return newArray
        
        
    #solution3: from down to up , merge two arrays 
    #method "mergeTwoArrays" is same as solution2
    def solution3(self, arrays):
        if not arrays:
            return []
            
        while len(arrays)>1:
            newArrays = []
            for i in range(0, len(arrays),2):
                if i+1<len(arrays):
                    newArray = self.mergeTwoArrays(arrays[i], arrays[i+1])
                else:
                    newArray = arrays[i]
                newArrays.append(newArray)
                
            arrays = newArrays
            
        return arrays[0]
