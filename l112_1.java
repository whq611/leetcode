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

public class l112_1 {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root==null) return false;
        Queue<Integer> num = new LinkedList<Integer>();
        Queue<TreeNode> nod = new LinkedList<TreeNode>();
        num.offer(root.val);
        nod.offer(root);
        while(!num.isEmpty()){
            int nums = num.poll();
            TreeNode node = nod.poll();
            if(node.left==null && node.right==null && targetSum==nums) return true;
            if(node.left!=null){
                num.offer(nums+node.left.val);
                nod.offer(node.left);
            }
            if(node.right!=null){
                num.offer(nums+node.right.val);
                nod.offer(node.right);
            }
        }
        return false;
    }
}
