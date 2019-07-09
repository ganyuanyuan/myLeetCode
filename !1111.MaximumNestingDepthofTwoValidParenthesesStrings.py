class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """

        depth , cur = 0, 0
        for c in seq:
            if c == '(':
                cur +=1
                depth = max(depth, cur)
            else:
                cur -= 1

        half = depth/2
        cur = 0
        ans = [0 for _ in range(len(seq))]
        for i, c in enumerate(seq):
            if c == '(':
                cur +=1
                if cur > half:
                    ans[i] = 1
            else:
                if cur > half:
                    ans[i] = 1
                cur -=1

        return ans


################################
# split the deepest part to 2 parts, and the depth of seperated parts is no more than half of depth.
# other parts will also success.
