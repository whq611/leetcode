class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public class l617 {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if(root1==null) return root2;
        if(root2==null) return root1;
        TreeNode root = new TreeNode(root1.val+root2.val);
        root.left = mergeTrees(root1.left,root2.left);
        root.right = mergeTrees(root1.right,root2.right);
        return root;
    }
}
