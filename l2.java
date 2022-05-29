class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

public class l2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode();
        ListNode cur = res;
        int i = 0, j = 0, a = 0, b = 0;
        while(l1!=null || l2!=null || b!=0){
            if(l1!=null){
                i = l1.val;
                l1 = l1.next;
            }
            else i = 0;
            if(l2!=null){
                j = l2.val; 
                l2 = l2.next;
            }
            else j = 0;
            a = (b+i+j)%10;
            b = (b+i+j)/10;
            cur.next = new ListNode(a);
            cur = cur.next;
            
        }
        return res.next;
    }
}
