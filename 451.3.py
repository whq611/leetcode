import collections
class Solution:
    def frequencySort(self, s):
        s = list(s)
        c = dict(collections.Counter(s).most_common())
        a = ''
        for (key,value) in c.items():
            a += key * value
        return a
