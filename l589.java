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
public class l589 {
    public List<Integer> preorder(Node root) {
        if(root==null) return new ArrayList<Integer>();
        List<Integer> res = new ArrayList<Integer>();
        res.add(root.val);
        for(Node child: root.children){
            res.addAll(preorder(child));
        }
        return res;
    }
}
