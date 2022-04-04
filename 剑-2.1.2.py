class Solution:
    def divide(self, a, b):
        INT_MAX,INT_MIN = -2**31,2**31-1
        if a == INT_MIN and b == -1:
            return INT_MAX
        ans = 0
        if b == INT_MIN:
            if a==b:
                return 1
            else:
                return 0
        if a == INT_MIN:
            a -= -abs(b)
            ans += 1
        sign = -1 if (a>0)^(b>0) else 1
        a,b = abs(a),abs(b)
        for i in range(31,-1,-1):
            if (a>>i)-b>=0:
                a = a - (b<<i)
                if ans > INT_MAX - (1<<i):
                    return INT_MIN
                ans + 1<<i
        return ans if sign==1 else -ans
