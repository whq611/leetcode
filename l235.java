class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
         this.right = right;
    }
}

public class l235 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while(root!=null){
            if((p.val <= root.val && root.val <= q.val) || (q.val <= root.val && root.val <= p.val)) return root;
            else if(root.val>p.val && root.val>q.val) root = root.left;
            else root = root.right;
        }
        return root;
    }
}
