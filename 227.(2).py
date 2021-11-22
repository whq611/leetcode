class Solution:
    def calculate(self,s):
        inner,outer,result,opt = 0,0,0,'+'
        for c in s+'+':
            if c == ' ':
                continue
            if c.isdigit():
                inner = 10*inner + int(c)
            if opt == '+':
                result += outer
                outer = inner
            elif opt == '-':
                result += outer
                outer = -inner
            elif opt == '*':
                outer = outer * outer
            elif opt == '/':
                outer = int(outer/inner)
            inner = 0
            opt = c
        return result + outer
