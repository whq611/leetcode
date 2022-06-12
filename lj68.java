class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class lj68 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode node = root;
        while(true){
            if(node.val>p.val && node.val>q.val) node = node.left;
            else if(node.val<p.val && node.val<q.val) node = node.right;
            else break;
        }
        return node;
    }
}
