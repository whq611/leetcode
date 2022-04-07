class Solution:
    def countBits(self, n):
        res = []
        a = 0
        for i in range(n+1):
            for j in '{0:b}'.format(i):
                if j == '1':
                    a += 1
            res.append(a)
            a = 0
        return res
