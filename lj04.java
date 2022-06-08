public class lj04 {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        int i = matrix.length-1, j = 0;
        while(i>=0 && j<matrix[0].length){
            if(matrix[i][j] == target) return true;
            else if(matrix[i][j] > target) i-=1;
            else j+=1;
        }
        return false;
    }
}
