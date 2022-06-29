import java.util.HashMap;

import java.util.Map;


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
public class l236_1 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode cur = root, p1 = p, q1 = q;
        Map<TreeNode,TreeNode> dic = new HashMap<>();
        dfs(cur, dic);
        while(p1!=q1){
            if(dic.containsKey(p1)) p1 = dic.get(p1);
            else p1 = q;
            if(dic.containsKey(q1)) q1 = dic.get(q1);
            else q1 = p;
        }
        return q1;
            
        
    }
    private void dfs(TreeNode cur, Map<TreeNode,TreeNode> dic){
        if(cur.left!=null){
            dic.put(cur.left,cur);
            dfs(cur.left,dic);
        }
        if(cur.right!=null){
            dic.put(cur.right,cur);
            dfs(cur.right,dic);
        }
    }
}
