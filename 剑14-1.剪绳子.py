import math
class Solution:
    def cuttingRope(self,n):
        if n<=3:
            return n-1
        a = n//3
        b = n%3
        if b == 0:
            return int(math.pow(3,a))
        elif b == 1:
            return int(math.pow(3,a-1)*4)
        else:
            return int(math.pow(3,a)*2)
