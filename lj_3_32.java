import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
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

public class lj_3_32 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        if(root==null) return list;
        queue.offer(root);
        int a = 1;
        while(!queue.isEmpty()){
            List<Integer> cur = new ArrayList<Integer>();
            int n = queue.size();
            for(int i=0; i<n; i++){
                TreeNode node = queue.poll();
                cur.add(node.val);
                if(node.left!=null) queue.offer(node.left);
                if(node.right!=null) queue.offer(node.right);
            }
            if(a%2==0) Collections.reverse(cur);
            list.add(cur);
            a+=1;
        }
        return list;
    }
}
