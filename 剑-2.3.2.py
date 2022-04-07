class Solution:
    def countBits(self, n):
        bits = [0]
        highbit = 0
        for i in range(1,n+1):
            if i & (i-1) == 0:
                highbit = i
            bits.append(bits[i-highbit]+1)
        return bits
