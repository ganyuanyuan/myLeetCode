class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        rev = ''
        for i in range(len(num)-1,-1,-1):
            if num[i]== '6':
                rev += '9'
            elif num[i] == '9':
                rev += '6'
            elif num[i] in set(['2','3','4','5','7']):
                return False
            else :
                rev += num[i]
        if rev == num:
            return True
        else:
            return False
