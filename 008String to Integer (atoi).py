class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        temp = str.lstrip()
        if len(temp)==0:
            return 0
        numbers = set(['0','1','2','3','4','5','6','7','8','9'])

        ans = ''
        i = 0
        ifnegative = None
        if temp[0]=='-':
            ifnegative = True
            i = 1
        elif temp[0]=='+':
            ifnegative = False
            i = 1
        else:
            ifnegative = False
        while i<len(temp):
            if temp[i] in numbers:
                ans += temp[i]
            else:
                break
            i += 1

        if len(ans)==0:
            return 0

        intans = int(ans)
        if ifnegative == True:
            if intans >2**31:
                return -2**31
            else:
                return -intans
        else:
            if intans >2**31-1:
                return 2**31-1
            else:
                return intans
