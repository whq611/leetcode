class Solution:
    def translateNum(self,num):
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            tmp = 10 * x + y
            if 10<=tmp<=25:
                c = a + b
            else:
                c = a
            b = a
            a = c
        return a
