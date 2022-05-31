class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = {}
        for i in magazine:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i in ransomNote:
            if i in a and a[i]>=1:
                a[i]-=1
            else:
                return False
        return True
