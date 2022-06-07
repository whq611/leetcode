class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        a = 31
        while a>=0:
            res |= (n&1)<<a
            n>>=1
            a-=1
        return res
