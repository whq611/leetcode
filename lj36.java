import java.util.LinkedList;

class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

public class lj36 {
    public Node treeToDoublyList(Node root) {
        if(root==null) return null;
        Node head = null, node = root, cur = null;
        LinkedList<Node> stack = new LinkedList<>();
        while(!stack.isEmpty() || node!=null){
            if(node!=null){
                stack.add(node);
                node = node.left;
            }
            else{
                node = stack.removeLast();
                if(head==null){
                    head = node;
                    cur = node;
                }
                else{
                    cur.right = node;
                    node.left = cur;
                    cur = cur.right;
                }
                node = node.right;
            }
            
        }
        cur.right = head;
        head.left = cur;
        return head;
    }
}
