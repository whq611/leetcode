public class lj29 {
    public int[] spiralOrder(int[][] matrix) {
        if(matrix.length==0) return new int[0];
        int n = matrix.length, m = matrix[0].length;
        int l = 0, r = m-1, t = 0, b = n-1;
        int[] res = new int[m*n];
        int j = 0;
        while(true){
            for(int i = l; i<r+1; i++){
                res[j++] = matrix[t][i];
            }
            t++;
            for(int i=t; i<b+1; i++){
                res[j++] = matrix[i][r];
            }
            r--;
            if(l>r || t>b) break;
            for(int i=r; i>l-1; i--){
                res[j++] = matrix[b][i];
            }
            b--;
            for(int i=b; i>t-1; i--){
                res[j++] = matrix[i][l];
            }
            l++;
            if(l>r || t>b) break;
        }
        return res;
    }
}
