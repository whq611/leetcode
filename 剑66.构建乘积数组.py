class Solution:
    def constructArr(self, a):
        tot = 1
        b = set()
        for i in range(len(a)):
            if a[i] != 0:
                tot *= a[i]
            else:
                b.add(i)
        if len(b)>1:
            return [0]*len(a)
        if len(b)==1:
            c = b.pop()
            return [0]*c+[tot]+[0]*(len(a)-c-1)
        res = []
        for i in a:
            res.append(int(tot/i))
        return res
