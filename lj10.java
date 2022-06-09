public class lj10 {
    public int fib(int n) {
        if(n==0) return 0;
        if(n==1) return 1;
        int slow = 0, fast = 1;
        while(n>1){
            int tmp = fast%1000000007;
            fast = (fast+slow)%1000000007;
            slow = tmp;
            n-=1;
        }
        return fast%1000000007;
    }
}
