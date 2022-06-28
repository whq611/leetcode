public class l74_1 {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix.length==0 || matrix[0].length==0) return false;
        int l = 0, r = matrix.length-1, i;
        while(l<=r){
            int m = l+(r-l)/2;
            if(matrix[m][0]>target) r = m-1;
            else l = m+1;
        }
        i = r;
        if(i<0) return false;
        l = 0;
        r = matrix[0].length-1;
        while(l<=r){
            int m = l+(r-l)/2;
            if(matrix[i][m]==target) return true;
            else if(matrix[i][m]>target) r = m-1;
            else l = m+1;
        }
        return false;
    }
}
