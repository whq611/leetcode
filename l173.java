import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
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
public class l173 {
    List<Integer> res = new ArrayList<>();
    int a = -1;
    int n;
    public l173(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode cur = root;
        while(cur!=null || !stack.isEmpty()){
            if(cur!=null){
                stack.add(cur);
                cur = cur.left;
            }
            else{
                cur = stack.pollLast();
                res.add(cur.val);
                cur = cur.right;
            }
        }
        this.n = res.size();
    }
    
    public int next() {
        a++;
        return res.get(a);
    }
    
    public boolean hasNext() {
        if(a+1>=n) return false;
        return true;
    }
}
