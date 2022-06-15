public class l48_1 {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for(int i=0; i<n/2; i++){
            for(int j=0; j<n; j++){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[n-i-1][j];
                matrix[n-i-1][j] = tmp;
                
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<i; j++){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
                
            }
        }
    }
}
