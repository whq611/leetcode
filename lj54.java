import java.util.ArrayList;
import java.util.List;
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class lj54 {
    public int kthLargest(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        dfs(root,res);
        return res.get(res.size()-k);
    }

    void dfs(TreeNode root, List<Integer> res){
        if(root==null) return;
        dfs(root.left,res);
        res.add(root.val);
        dfs(root.right,res);
        
    }
}
