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

public class lj27 {
    public TreeNode mirrorTree(TreeNode root) {
        if(root==null) return null;
        TreeNode rootA = new TreeNode(root.val);
        rootA.left = mirrorTree(root.right);
        rootA.right = mirrorTree(root.left);
        return rootA;
    }
}
