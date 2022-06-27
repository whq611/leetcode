import java.util.HashMap;
import java.util.Map;

public class l105 {
    int[] preorder;
    int[] inorder;
    Map<Integer,Integer> dic;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        int n = preorder.length;
        dic = new HashMap<Integer,Integer>();
        for(int i = 0; i<n; i++){
            dic.put(inorder[i], i);
        }
        return dfs(0,n-1,0,n-1);

    }

    public TreeNode dfs(int l1, int r1, int l2, int r2){
        if(l1>r1 || l2>r2) return null;
        TreeNode root = new TreeNode(preorder[l1]);
        int root_inorder = dic.get(preorder[l1]);
        root.left = dfs(l1+1,l1 + root_inorder - l2,l2,root_inorder-1);
        root.right = dfs(l1 + root_inorder - l2 + 1, r1, root_inorder+1,r2);

        return root;
    }
}
