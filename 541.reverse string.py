class Solution:
    def reverseStr(self, s, k):
        s = list(s)
        a = len(s) // (2*k)
        b = 0
        for i in range(a):
            c,d = b,b+k-1
            while c<d:
                s[c],s[d] = s[d],s[c]
                c += 1
                d -= 1
            b = b + 2*k
        e = len(s) - a*2*k
        if e <= k:
            f,g = a*2*k,len(s) - 1
            while f<g:
                s[f],s[g] = s[g],s[f]
                f += 1
                g -= 1
        else:
            f,g = a*2*k,a*2*k+k-1
            while f<g:
                s[f],s[g] = s[g],s[f]
                f += 1
                g -= 1
        return ''.join(s)
