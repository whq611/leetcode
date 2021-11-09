class Solution:
    def firstUniqChar(self, s):
        a,b = [],[]
        for i in range(len(s)):
            if s[i] in a and s[i] in b:
                b.remove(s[i])
            elif s[i] in a :
                continue
            else:
                a.append(s[i])
                b.append(s[i])
        if b:
            return b[0]
        else:
            return ' '
