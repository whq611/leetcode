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

public class l112 {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null) return false;
        targetSum -= root.val;
        if(root.left==null && root.right==null) return targetSum == 0;
        return hasPathSum(root.left, targetSum) || hasPathSum(root.right, targetSum);
    }
}
