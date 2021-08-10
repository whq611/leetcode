class Solution:
    def makeLargestSpecial(self, s):
        if not s:
            return ''
        length = len(s)
        count = 0
        a = []
        pre = 0

        for i in range(length):
            if s[i] == '1':
                count += 1
            elif s[i] == '0':
                count -= 1
            if count == 0:
                a.append('1' + self.makeLargestSpecial(s[pre+1:i]) + '0')
                pre = i + 1
        return ''.join(sorted(a,reverse = True))
