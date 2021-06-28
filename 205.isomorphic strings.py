class Solution:
    def isIsomorphic(self, s, t):
        a = dict()
        i = len(s) - 1
        while i >= 0:
            if s[i] in a:
                if t[i] != a[s[i]]:
                    return False
            if t[i] in a.values():
                 if list(a.keys())[list(a.values()).index(t[i])] != s[i]:
                     return False
            else:
                a[s[i]] = t[i]
            i -= 1
        return True
