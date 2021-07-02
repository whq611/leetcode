class Solution:
    def reverseVowels(self, s):
        a = 'aeiouAEIOU'
        s = list(s)
        l,r = 0,len(s)-1
        while l<r:
            if s[l] in a and s[r] in a:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
            if s[l] not in a:
                l += 1
            if s[r] not in a:
                r -= 1
        return ''.join(s)
