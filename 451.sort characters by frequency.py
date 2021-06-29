from collections import Counter
class Solution:
    def frequencySort(self, s):
        s = list(s)
        c = dict(Counter(s).most_common())
        a = ''
        for (key,value) in c.items():
            while value > 0:
                a = a + key
                value -= 1
        return a
