# without any loop/recursion in O(1) runtime
# related to 9
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num %9 ==0 and num!=0:
            return 9
        else:
            return num%9

# recursion solution
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def myrecursion(n):
            if n < 10:
                return n
            ans = 0
            while n//10>0:
                ans += n % 10
                n = n//10
            ans += n
            return myrecursion(ans)
        return myrecursion(num)
