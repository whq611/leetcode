import java.util.Arrays;
import java.util.LinkedList;

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
public class l297_1 {
    public String serialize(TreeNode root) {
        return dfs(root);
    }
    public String dfs(TreeNode root){
        if(root==null) return "None ";
        return String.valueOf(root.val) + " " + dfs(root.left) + dfs(root.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        LinkedList<String> res = new LinkedList<> (Arrays.asList(data.split(" ")));

        return ddfs(res);
    }
    public TreeNode ddfs(LinkedList<String> res){
        
        String node = res.poll();
        if(node.equals("None")) return null;
        TreeNode a = new TreeNode(Integer.parseInt(node));
        a.left = ddfs(res);
        a.right = ddfs(res);
        return a;
        
    }
}
