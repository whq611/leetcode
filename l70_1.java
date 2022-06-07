public class l70_1 {
    public int climbStairs(int n) {
        int slow = 1, fast = 1;
        while(n>0){
            int tmp = fast;
            fast = slow + fast;
            slow = tmp;
            n-=1;
        }
        return slow;
    }
}
