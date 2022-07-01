import java.util.ArrayList;
import java.util.List;
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};

public class l589_1 {
    List<Integer> res;
    public List<Integer> preorder(Node root) {
        
        res = new ArrayList<Integer>();
        dfs(root);
        
        return res;
    }
    public void dfs(Node root){
        if(root==null) return;
        res.add(root.val);
        for(Node child: root.children){
            dfs(child);
        }
    }
}
