public class lj17 {
    public int[] printNumbers(int n) {
        int[] res = new int[(int) Math.pow(10,n)-1];
        for(int i = 1; i<Math.pow(10,n); i++){
            res[i-1] = i;
        }
        return res;
    }
}
