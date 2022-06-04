import java.util.LinkedList;

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

public class l102_1 {
    List<List<Integer>> res = new LinkedList<List<Integer>>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root==null) return res;
        helper(root,0);
        return res;
    }

    public void helper(TreeNode node, int level){
        if(res.size()==level) res.add(new LinkedList<Integer>());
        res.get(level).add(node.val);
        if(node.left!=null) helper(node.left,level+1);
        if(node.right!=null) helper(node.right,level+1);
    }
}
