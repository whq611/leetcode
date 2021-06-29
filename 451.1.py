class Solution:
    def frequencySort(self, s):
        counter = {}
        a = []
        res = ''
        for c in s:
            counter[c] = counter.get(c,0) + 1
        for key,val in counter.items():
            a.append((-val,key))
        for val,key in sorted(a):
            res += key * (-val)
        return res
