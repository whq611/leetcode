public class lj2_3 {
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        for(int i=1;i<n+1;i++)
            res[i] = res[i>>1] + (i%2);
        return res;
    }
}
