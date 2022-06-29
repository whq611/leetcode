import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;

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
public class l236 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode cur = root;
        Map<TreeNode,TreeNode> dic = new HashMap<>();
        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.add(cur);
        while(!stack.isEmpty()){
            cur = stack.poll();
            if(cur.left!=null){
                dic.put(cur.left,cur);
                stack.add(cur.left);
            }
            if(cur.right!=null){
                dic.put(cur.right,cur);
                stack.add(cur.right);
            }
        }
        Set<TreeNode> a = new HashSet<>();
        while(dic.containsKey(p)){
            a.add(p);
            p = dic.get(p);
        }
        a.add(p);
        while(!a.contains(q)){
            q = dic.get(q);
        }
        return q;
            
        
    }
}
