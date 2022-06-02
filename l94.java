import java.util.ArrayList;
import java.util.List;
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
    }
}

public class l94 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        inorder(res,root);
        return res;
    }
    public void inorder(List<Integer> res, TreeNode root){
        if(root==null) return;
        inorder(res,root.left);
        res.add(root.val);
        inorder(res,root.right);
    }
}
