class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeToDoublyList(self,root):
        if not root:
            return None
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                sol.append(curr)
                curr = curr.right
        i,j = 0,1
        sol[0].left = sol[-1]
        sol[-1].right = sol[0]
        while j<len(sol):
            sol[i].right = sol[j]
            sol[j].left = sol[i]
            i += 1
            j += 1
        return sol[0]
