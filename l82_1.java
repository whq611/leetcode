class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class l82_1 {
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next==null) return head;
        if(head.val!=head.next.val) head.next = deleteDuplicates(head.next);
        else{
            ListNode move = head.next;
            while(move!=null && move.val==head.val) move = move.next;
            return deleteDuplicates(move);
        }
        return head;
    }
}
