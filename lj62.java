public class lj62 {
    public int lastRemaining(int n, int m) {
        int res = 0;
        for(int i=2; i<n+1; i++){
            res = (res+m)%i;
        }
        return res;
        

    }
}
