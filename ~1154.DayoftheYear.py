class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        date = date.split('-')
        year , month, day = int(date[0]), int(date[1]), int(date[2])
        if year%100 != 0 and year%4==0:
            flag = 1
        elif year % 400 ==0 :
            flag = 1
        else:
            flag = 0

        res = 0
        for m in range(1,month):
            if m in [1,3,5,7,8,10,12]:
                res += 31
            elif m in [4,6,9,11]:
                res +=30
            else:
                res += 28 + flag
        return res + day 
