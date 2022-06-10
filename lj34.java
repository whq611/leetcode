import java.util.ArrayList;
import java.util.List;

public class lj34 {
    public List<List<Integer>> pathSum(TreeNode root, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        dfs(root, 0, target, cur, res);
        return res;
    }

    public void dfs(TreeNode node, int num, int target, List<Integer> cur, List<List<Integer>> res){
        if(node==null) return;
        num+=node.val;
        cur.add(node.val);
        if(node.left==null && node.right==null && num==target){
            res.add(new ArrayList<>(cur));
        }
        dfs(node.left, num, target, cur, res);
        dfs(node.right, num, target, cur, res);
        cur.remove(cur.size()-1);
        num-=node.val;
    }
}
