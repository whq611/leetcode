import java.util.LinkedList;
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
public class jian06 {
    public int[] reversePrint(ListNode head) {
        LinkedList<Integer> stack = new LinkedList<Integer>();
        while(head != null) {
            stack.addLast(head.val);
            head = head.next;
        }
        int[] res = new int[stack.size()];
        for(int i = 0; i < res.length; i++)
            res[i] = stack.get(i);
        
    return res;
    }
}
