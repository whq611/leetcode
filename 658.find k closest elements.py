import collections
class Solution:
    def findClosestElements(self, arr, k, x):
        s = collections.defaultdict(int)
        j = 0
        for i in arr:
            a = i - x
            if a < 0:
                a = -a
            s[j] = a
            j += 1
        b = sorted((value, key) for (key, value) in s.items())
        
        c = []
        for i in b:
            if k > 0:
                c.append(arr[i[1]])
                k -= 1
        return sorted(c)
