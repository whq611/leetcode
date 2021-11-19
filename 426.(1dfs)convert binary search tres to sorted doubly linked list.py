class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tressToDoublyList(self,root):
        if not root:
            return None
        stack = []
        first,last,curr = None,None,root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if not first:
                    first = curr
                if last:
                    last.right = curr
                    curr.left = last
                last = curr
                curr = curr.right
        first.left = last
        last.right = first

        return first
