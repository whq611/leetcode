class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i in t:
            if i in a and a[i]>=1:
                a[i]-=1
                if a[i] == 0:
                    a.pop(i)
            else:
                return False
        return not a
