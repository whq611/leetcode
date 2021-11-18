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
        s = list(s)
        stack1 += stack2
        stack1.sort()
        cnt = 0
        for i in stack1:
            s.pop(i-cnt)
            cnt += 1
        return ''.join(s)
