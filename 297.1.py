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
        def dfs(root):
            if not root: return 'None '
            return str(root.val)+' ' + dfs(root.left) + dfs(root.right);
        
        return dfs(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(data):
            node = data.popleft()
            if node == 'None': return
            a = TreeNode(int(node))
            a.left = dfs(data)
            a.right = dfs(data)

            return a
        
        data = collections.deque(data.split())

        
        return dfs(data)
        
        



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
