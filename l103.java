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

public class l103 {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if(root==null) return new ArrayList<>();
        int a = 0;
        LinkedList<TreeNode> cur = new LinkedList<>();
        cur.add(root);
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> b = new ArrayList<>();
        b.add(root.val);
        res.add(b);
        while(true){
            List<Integer> x = new ArrayList<>();
            List<TreeNode> nex = new LinkedList<>();
            while(!cur.isEmpty()){
                TreeNode node = cur.removeFirst();
                if(node.left!=null){
                    nex.add(node.left);
                    x.add(node.left.val);
                }
                if(node.right!=null){
                    nex.add(node.right);
                    x.add(node.right.val);
                }
                
            }
            if(x.isEmpty()) break;
            if(a%2==0) Collections.reverse(x);
            res.add(x);
            a+=1;
            cur = new LinkedList<>(nex);

        }
        return res;

    }
}
