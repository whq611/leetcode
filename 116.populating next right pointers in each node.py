class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        cur = collections.deque([root])
        nex = collections.deque([])
        while cur:
            while cur:
                node = cur.popleft()
                if node.left: nex.append(node.left)
                if node.right: nex.append(node.right)
            if nex:
                for i in range(len(nex)-1):
                    nex[i].next = nex[i+1]
            cur = nex
            nex = collections.deque([])
        return root
