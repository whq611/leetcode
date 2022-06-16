public class l59 {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int l = 0, r = n-1, t = 0, b = n-1;
        int m = 1;
        while(true){
            for(int i = l; i<r+1; i++){
                res[t][i] = m++;
            }
            t++;
            for(int i=t; i<b+1; i++){
                res[i][r] = m++;
            }
            r--;
            for(int i=r; i>l-1; i--){
                res[b][i] = m++;
            }
            b--;
            for(int i=b; i>t-1; i--){
                res[i][l] = m++;
            }
            l++;
            if(l>r || t>b) break;
        }
        return res;
    }
}
