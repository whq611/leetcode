import collections
class Solution:
    def firstUniqChar(self, s):
        frequency = collections.Counter(s)
        for i,val in dict(frequency).items():
            if val == 1:
                return i
        return ' '
