import java.util.Stack;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class lj2_25_1 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> s1 = new Stack<>();
        Stack<Integer> s2 = new Stack<>();
        while(l1!=null){
            s1.push(l1.val);
            l1 = l1.next;
        }
        while(l2!=null){
            s2.push(l2.val);
            l2 = l2.next;
        }
        ListNode head=null;
        int carry = 0, val = 0, x = 0, y = 0;
        while(!s1.isEmpty() || !s2.isEmpty() || carry!=0){
            x = !s1.isEmpty() ? s1.pop(): 0;
            y = !s2.isEmpty() ? s2.pop(): 0;
            val = (x+y+carry)%10;
            carry = (x+y+carry)/10;
            ListNode curr = new ListNode(val);
            curr.next = head;
            head = curr;
        }
        return head;
    }
}
