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

public class lj_3_32_1 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> list = new LinkedList<List<Integer>>();
        if(root==null) return list;
        list.add(new ArrayList<Integer>());
        if(root==null) return list;
        helper(root, 0, list);
        list.remove(list.size()-1);
        for(int i=0; i<list.size(); i++){
            if(i%2==1) Collections.reverse(list.get(i));
        }
        return list;
    }
    public void helper(TreeNode node, int level, List<List<Integer>> list){
        if(node==null) return;
        list.get(level).add(node.val);
        if(list.size()==level+1) list.add(new ArrayList<Integer>());
        helper(node.left,level+1,list);
        helper(node.right,level+1,list);
    }
}
