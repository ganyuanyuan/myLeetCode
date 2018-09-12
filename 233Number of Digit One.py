class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=0:
            return 0
        ans = 0
        strn = str(n)
        lenth = len(strn)
        for i in range(lenth):
            if int(strn[i])>1:
                ans += (int(strn[i]))*(lenth-i-1)*10**(lenth-i-2) + 10**(lenth-i-1)
            elif int(strn[i])==1:
                ans += (lenth-i-1)*10**(lenth-i-2) + (int(strn[i:])-int('0'+'9'*(lenth-i-1)))


        return int(ans)
