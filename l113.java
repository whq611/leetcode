import java.util.ArrayList;

import java.util.LinkedList;
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

public class l113 {
    List<List<Integer>> res = new ArrayList<>();
    LinkedList<Integer> cur = new LinkedList<>();
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if(root==null) return res;
        dfs(root, targetSum, cur); 
        return res;      
    }

    private void dfs(TreeNode root, int targetSum, LinkedList<Integer> cur){
        targetSum -= root.val;
        cur.add(root.val);
        if(root.left==null && root.right==null && targetSum == 0) res.add(new ArrayList<>(cur));
        if(root.left!=null){
            dfs(root.left, targetSum, cur);
            cur.pollLast();
        }
        if(root.right!=null){
            dfs(root.right, targetSum, cur);
            cur.pollLast();
        }
    }
}