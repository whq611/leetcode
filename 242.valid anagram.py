class Solution:
    def isAnagram(self, s, t):
        t = list(t)
        for i in s:
            if i in t:
                t.remove(i)
            else:
                return False
        return t == []
