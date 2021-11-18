class Solution:
    def minRemoveToMakeValid(self, s):
        stack1 = []
        stack2 = []
        for i in range(len(s)):
            if s[i] == '(':
                stack1.append(i)
            elif s[i] == ')':
                if stack1:
                    stack1.pop()
                else:
                    stack2.append(i)
        c = []
        stack1 = set(stack1).union(set(stack2))
        for i,j in enumerate(s):
            if i not in stack1:
                c.append(j)
        return ''.join(c)
