class Solution:
    def minAddToMakeValid(self, s):
        a = 0
        b = 0
        for i in s:
            if i == '(':
                a += 1
            if i == ')':
                if a == 0:
                    b += 1
                else:
                    a -= 1
        return a+b
