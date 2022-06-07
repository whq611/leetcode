import java.util.ArrayList;
import java.util.List;
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

public class l98 {
    public boolean isValidBST(TreeNode root) {
        List<Integer> a = new ArrayList<>();
        inorder(a,root);
        int i = a.size()-1;
        while(i>0){
            if(a.get(i-1)>=a.get(i)) return false;
            i-=1;
        }
        return true;
    }

    public void inorder(List<Integer> res, TreeNode root){
        if(root==null) return;
        inorder(res,root.left);
        res.add(root.val);
        inorder(res,root.right);
    }
}
