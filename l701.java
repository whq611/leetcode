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

public class l701 {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root==null) return new TreeNode(val);
        TreeNode node = root;
        while(node!=null){
            if(val>node.val){
                if(node.right==null){
                    node.right = new TreeNode(val);
                    return root;
                }
                else node = node.right;
            }
            else{
                if(node.left==null){
                    node.left = new TreeNode(val);
                    return root;
                }
                else node = node.left;
            }
        }
        return root;
    }
}
