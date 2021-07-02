class Solution:
    def reverseVowels(self, s):
        x = 'aeiouAEIOU'
        a = []
        ls = [i for i in s if i in x]
        for k in s:
            if k not in x:
                a.append(k)
            else:
                a.append(ls.pop())
        return''.join(a)
