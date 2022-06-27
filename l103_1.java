import java.util.ArrayList;
import java.util.Collections;
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

public class l103_1 {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if(root==null) return new ArrayList<>();
        int a = 0;
        LinkedList<TreeNode> cur = new LinkedList<>();
        cur.add(root);
        List<List<Integer>> res = new ArrayList<>();
        
        while(!cur.isEmpty()){
            List<Integer> x = new ArrayList<>();
            List<TreeNode> nex = new LinkedList<>();
            while(!cur.isEmpty()){
                TreeNode node = cur.removeFirst();
                x.add(node.val);
                if(node.left!=null){
                    nex.add(node.left);
                    
                }
                if(node.right!=null){
                    nex.add(node.right);
                    
                }
                
            }
            
            if(a%2==1) Collections.reverse(x);
            res.add(x);
            a+=1;
            cur = new LinkedList<>(nex);

        }
        return res;

    }
}
