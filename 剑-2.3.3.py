class Solution:
    def countBits(self, n):
        bits = [0]
        for i in range(1,n+1):
            bits.append(bits[i>>1] + (i&1))
        return bits
