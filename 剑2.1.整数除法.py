class Solution:
    def divide(self, a, b):
        INT_MIN, INT_MAX = -2**31, 2**31-1
        if a == INT_MIN and b == -1:
            return INT_MAX
        if (a>0)^(b>0):
            sign = -1
        else:
            sign = 1
        if a>0:
            a = -a
        if b>0:
            b = -b
        ans = 0
        while a<=b:
            a -= b
            ans += 1
        if sign == 1:
            return ans
        else:
            return -ans
