class Solution:
    def reverseStr(self, s, k):
        s = list(s)
        a = len(s) // (2*k) + 1
        b = 0
        for i in range(a):
            s[b:b+k] = reversed(s[b:b+k])
            b = b + 2*k
        return ''.join(s)
