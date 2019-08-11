class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if d*f < target:
            return 0

        mod = (10**9+7)


        prev = [0 for _ in range(target+1)]
        for i in range(1,min(f, target)+1):
            prev[i] = 1

        curr = [0 for _ in range(target+1)]
        for i in range(d-1):
            for k in range(1, f+1):
                for j in range(target+1):
                    if j-k>0:
                        curr[j] = (curr[j] +prev[j-k])% mod
            prev = curr
            curr = [0 for _ in range(target+1)]

        return prev[-1] % mod
