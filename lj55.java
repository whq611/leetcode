class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}


public class lj55 {
    public boolean isBalanced(TreeNode root) {
        if(root==null) return true;
        return Math.abs(height(root.left)-height(root.right))<=1 && isBalanced(root.left) && isBalanced(root.right);
    }

    private int height(TreeNode node){
        if(node==null) return 0;
        return Math.max(height(node.left), height(node.right)) + 1;
    }
}
