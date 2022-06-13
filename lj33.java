import java.util.Deque;
import java.util.LinkedList;

public class lj33 {
    public boolean verifyPostorder(int[] postorder) {
        Deque<Integer> stack = new LinkedList<>();
        int root = Integer.MAX_VALUE;
        for(int i=postorder.length-1;i>=0;i--){
            if(postorder[i]>root) return false;
            while(!stack.isEmpty() && postorder[i]<stack.peek()){
                root = stack.pop();
            }
            stack.push(postorder[i]);
        }
        return true;
    }
}
