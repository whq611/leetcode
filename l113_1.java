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

public class l113_1 {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> res = new ArrayList<>();
        if(root==null) return res;
        LinkedList<Integer> num = new LinkedList<Integer>();
        LinkedList<TreeNode> nod = new LinkedList<TreeNode>();
        LinkedList<LinkedList<Integer>> path = new LinkedList<>();
        num.add(root.val);
        nod.add(root);
        path.add(new LinkedList<>(num));
        while(!num.isEmpty()){
            int nums = num.poll();
            TreeNode node = nod.poll();
            LinkedList cur = path.poll();
            if(node.left==null && node.right==null && targetSum==nums) res.add(new LinkedList<>(cur));
            if(node.left!=null){
                num.add(nums+node.left.val);
                nod.add(node.left);
                cur.add(node.left.val);
                path.add(new LinkedList<>(cur));
                cur.pollLast();
            }
            if(node.right!=null){
                num.add(nums+node.right.val);
                nod.add(node.right);
                cur.add(node.right.val);
                path.add(new LinkedList<>(cur));
                cur.pollLast();
            }
        }
        return res;
    }
}
