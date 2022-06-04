import java.util.LinkedList;
import java.util.Queue;

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

public class l102 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        if(root==null) return res;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        while(!queue.isEmpty()){
            int q = queue.size();
            List<Integer> cur = new LinkedList<Integer>();
            for(int i=0; i<q;i++){
                TreeNode a = queue.poll();
                cur.add(a.val);
                if(a.left!=null) queue.offer(a.left);
                if(a.right!=null) queue.offer(a.right);
            }
            res.add(cur);
        }
        return res;
    }
}
