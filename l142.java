import java.util.HashSet;
import java.util.Set;
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}
public class l142 {
    public ListNode detectCycle(ListNode head) {
        if(head==null) return null;
        Set<ListNode> a = new HashSet<>();
        while(head!=null){
            if(a.contains(head)) return head;
            a.add(head);
            head = head.next;
        }
        return null;
    }
}
