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
public class l297 {
    public String serialize(TreeNode root) {
        StringBuffer res = new StringBuffer();
        LinkedList<TreeNode> cur = new LinkedList<>();
        cur.add(root);
        TreeNode node;
        while(!cur.isEmpty()){
            node = cur.poll();
            if(node!=null){
                res.append(String.valueOf(node.val)+" ");
                cur.add(node.left);
                cur.add(node.right);
            }
            else res.append("None ");
        }

        return res.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] res = data.split(" ");

        String a = res[0];
        if(a.equals("None")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(a));
        TreeNode cur;
        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.add(root);
        int i = 1;
        while(i<res.length){
            for(int j=0; j<stack.size(); j++){
                a = res[i++];
                cur = stack.poll();
                if(!a.equals("None")){
                    cur.left = new TreeNode(Integer.parseInt(a));
                    stack.add(cur.left);
                }
                a = res[i++];
                
                if(!a.equals("None")){
                    cur.right = new TreeNode(Integer.parseInt(a));
                    stack.add(cur.right);
                }
            }
        }
        return root;
    }
}
