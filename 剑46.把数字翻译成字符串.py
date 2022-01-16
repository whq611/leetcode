class Solution:
    def translateNum(self,num):
        s = str(num)
        a = b = 1
        for i in range(2,len(s)+1):
            tmp = s[i-2:i]
            if '10'<=tmp<='25':
                c = a + b
            else:
                c = a
            b = a
            a = c
        return a
