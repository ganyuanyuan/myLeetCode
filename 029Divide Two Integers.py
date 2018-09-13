class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ispositive = None
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            ispositive =True
        elif (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            ispositive = False
        else:
            return 0

        ans = 0
        x = abs(dividend)
        y = abs(divisor)
        m = len(str(x))
        n = len(str(y))
        anslist = []
        addzero = []
        while x>=y:
            for i in range(n-1,m):
                if int(str(x)[:i+1])>=y:
                    temp = int(str(x)[:i+1])
                    res = 0
                    while temp>=y:
                        temp -=y
                        res +=1
                    anslist.append(res)
                    addzero.append(len(str(x)[i+1:]))
                    x = int(str(temp)+str(x)[i+1:])
                    break
        if len(addzero)==0:
            pass
        elif addzero[0]+1 > len(addzero):
            for i in range(len(addzero)-1):
                if addzero[i]-addzero[i+1]>1:
                    for j in range(1,addzero[i]-addzero[i+1]):
                        anslist.insert(i+1,0)
            if addzero[-1]!=0:
                for j in range(addzero[-1]):
                    anslist.append(0)

        res = '0'
        for i in anslist:
            res += str(i)
        ans = int(res)
        if ispositive :
            if ans > 2**31-1:
                return 2**31-1
            else:
                return ans
        else:
            if ans>2**31:
                return -2**31
            else:
                return -ans
