class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self,root):
        if not root:
            return ' '
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self,data):
        def helper(nodes):
            if not nodes:
                return None
            val = nodes.pop()
            if val == ' ':
                node = None
            else:
                node = TreeNode(int(val))
                node.left = helper(nodes)
                node.right = helper(nodes)
            return node
        data = data.split(',')
        return helper(data)
