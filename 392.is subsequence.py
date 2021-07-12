class Solution:
    def isSubsequence(self, s, t):
        b = 0
        for i in s:
            if t.find(i,b) >= 0:
                b = t.find(i,b) + 1
            else:
                return False
        return True
