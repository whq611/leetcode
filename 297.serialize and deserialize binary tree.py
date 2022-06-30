# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        cur = collections.deque([root])
        while cur:
            node = cur.popleft()
            if node:
                res+=str(node.val)+' '
                cur.append(node.left)
                cur.append(node.right)
            else: res+='None '
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data = collections.deque(data.split())

        a = data.popleft()
        if a=='None': return None
        root = TreeNode(int(a))
        stack = collections.deque([root])
        while data:
            for i in range(len(stack)):
                cur = stack.popleft()
                a = data.popleft()
                if a!='None':
                    cur.left = TreeNode(int(a))
                    stack.append(cur.left)
                a = data.popleft()
                if a!='None':
                    cur.right = TreeNode(int(a))
                    stack.append(cur.right)
        return root
