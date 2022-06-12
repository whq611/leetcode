import java.util.HashMap;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class lj_2_68 {
    HashMap<TreeNode,TreeNode> ancestor = new HashMap<TreeNode,TreeNode>(); 
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        dfs(root);
        TreeNode p1 = p, q1 = q;
        while(true){
            if(p1.equals(q1)) return p1;
            if(ancestor.containsKey(p1)) p1 = ancestor.get(p1);
            else p1 = q;
            if(ancestor.containsKey(q1)) q1 = ancestor.get(q1);
            else q1 = p;
        }
    }

    private void dfs(TreeNode root){
        if(root==null) return;
        if(root.left!=null){
            ancestor.put(root.left,root);
            dfs(root.left);
        }
        if(root.right!=null){
            ancestor.put(root.right,root);
            dfs(root.right);
        }
    }
}
