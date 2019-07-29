class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        monoStack = []
        res = 0
        A = [0] + A + [0]
        for i in range(len(A)):
            while monoStack and A[monoStack[-1]] > A[i]:
                j = monoStack.pop()
                k = monoStack[-1]
                res += A[j] * (i-j) *(j-k)
            monoStack.append(i)
        return res % (10**9+7)



#############################################################################
#
#       for every index:j, it contributes the A[j] * (i-j) * (j-k)
#                                                     |         |
#                                                    next      prev
#                                                   smaller   smaller
#
##############################################################################
