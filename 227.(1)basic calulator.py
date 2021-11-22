class Solution:
    def calculate(self,s):
        stack = []
        curr = 0
        ope = '+'
        if not s:
            return 0
        operators = {'+','-','*','/'}
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                curr = curr*10 + int(char)
            elif char in operators or i == len(s) -1:
                if ope == '+':
                    stack.append(curr)
                elif ope == '-':
                    stack.append(-curr)
                elif ope == '*':
                    stack[-1] *= curr
                elif ope == '/':
                    stack[-1] = int(stack[-1]/curr)
                curr = 0
                ope = char
        return sum(stack)
                    
                
