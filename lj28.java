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

public class lj28 {
    public boolean isSymmetric(TreeNode root) {
        if(root==null) return true;
        return recur(root.left,root.right);
    }
    private boolean recur(TreeNode l, TreeNode r){
        if(l==null && r==null) return true;
        if((l==null && r!=null) || (l!=null && r==null) || (l.val!=r.val)) return false;
        return recur(l.left,r.right) && recur(l.right,r.left);
    }
}
