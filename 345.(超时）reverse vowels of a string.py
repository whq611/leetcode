class Solution:
    def reverseVowels(self, s):
        a = {}
        s = list(s)
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                a[i] = s[i]
        i = 0
        for key in a:
            s[key] = list(a.values())[::-1][i]
            i += 1
        return ''.join(s)
