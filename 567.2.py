class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        diff = 0
        if n>m:
            return False
        cnt1 = [0] * 26
        for i in range(n):
            cnt1[ord(s1[i]) - ord('a')] -= 1
        left = right = 0
        while right<m:
            x = ord(s2[right]) - ord('a')
            cnt1[x] += 1
            while cnt1[x]>0:
                cnt1[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if right - left + 1 == n:
                return True
            right += 1

        return False
