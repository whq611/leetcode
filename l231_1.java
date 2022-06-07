public class l231_1 {
    public boolean isPowerOfTwo(int n) {
        if(n<=0) return false;
        
        return (n & (-n)) == n;
    }
}
