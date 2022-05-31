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

public class l141 {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> a = new HashSet<>();
        while(head!=null){
            if(a.contains(head)) return true;
            a.add(head);
            head = head.next;
        }
        return false;
    }
}
