import java.util.ArrayList;
import java.util.Deque;
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

public class l199 {
    public List<Integer> rightSideView(TreeNode root) {
        if(root==null) return new ArrayList<Integer>();
        List<Integer> res = new ArrayList<Integer>();
        Deque<TreeNode> nex = new LinkedList<TreeNode>();
        Deque<TreeNode> cur;
        TreeNode node = new TreeNode();
        nex.offer(root);
        while(!nex.isEmpty()){
            cur = nex;
            nex = new LinkedList<TreeNode>();
            while(!cur.isEmpty()){
                node = cur.poll();
                if(node.left!=null) nex.offer(node.left);
                if(node.right!=null) nex.offer(node.right);
            }
            res.add(node.val);
        }
        return res;
    }
}
