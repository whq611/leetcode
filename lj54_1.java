class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class lj54_1 {
    int res, k;
    public int kthLargest(TreeNode root, int k) {
        this.k = k;
        dfs(root);
        return res;
    }

    void dfs(TreeNode root){
        if(root==null) return;
        dfs(root.right);
        if(k == 0) return;
        k-=1;
        if(k == 0) res = root.val;
        dfs(root.left);
}
}