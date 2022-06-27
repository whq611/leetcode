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

public class l108 {
    int[] nums;
    public TreeNode sortedArrayToBST(int[] nums) {
        this.nums = nums;
        return dfs(0,nums.length-1);
    }

    public TreeNode dfs(int l, int r){
        if(r<l) return null;
        int m = l+(r-l)/2;
        TreeNode root = new TreeNode(nums[m]);
        root.left = dfs(l,m-1);
        root.right = dfs(m+1,r);
        return root;
    }
}
