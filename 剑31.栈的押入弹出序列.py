class Solution:
    def validateStackSequences(self, pushed, popped):
        stack,i = [],0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
