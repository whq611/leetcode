class Solution:
    def removeDuplicates(self, s):
        stack = []
        for i in s:
            if stack:
                if i == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return ''.join(stack)
