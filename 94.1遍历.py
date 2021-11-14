class Solution:
    def inorderTraversal(self,root):
        stack = []
        sol = []
        cur = root
        while stack or curr:
            if curr:
                stack.append(curr)
                cur = cur.left
            else:
                curr = stack.pop()
                sol.append(curr.val)
                curr = curr.right
        return sol
