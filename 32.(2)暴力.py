class Solution():
    def longestValidParentheses(self,s):
        def isValid(x):
            stack = []
            for i in range(len(x)):
                if x[i] == '(':
                    stack.append('(')
                elif stack != [] and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return stack == []

        n = len(s)
        if n<2: return 0
        for i in range(n if n%2 == 0 else n-1,0,-2):
            for j in range(n-i+1):
                if isValid(s[j:j+i]):
                    return i
        return 0
