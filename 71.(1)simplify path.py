class Solution:
    def SimplifyPath(self,path):
        stack = []
        for i in path.split('/'):
            if i not in ['','.','..']:
                stack.append(i)
            elif stack and i == '..':
                stack.pop()
        return '/' + '/'.join(stack)
