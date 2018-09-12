class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        newset = set()

        while n != 1 :
            temp = 0
            for char in str(n):
                temp += int(char)**2

            if temp in newset:
                return False
            else:
                newset.add(temp)
            n = temp
        return True
