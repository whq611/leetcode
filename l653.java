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

public class l653 {
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> a = new ArrayList<>();
        inorder(a,root);
        int i = 0, j = a.size()-1;
        while(i<j){
            if(a.get(i)+a.get(j)==k) return true;
            else if(a.get(i)+a.get(j)<k) i++;
            else j--;
        }
        return false;
    }

    private void inorder(List<Integer> a, TreeNode node){
        if(node==null) return;
        inorder(a,node.left);
        a.add(node.val);
        inorder(a,node.right);
    }
}
