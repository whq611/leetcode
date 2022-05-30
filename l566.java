public class l566 {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        if(mat.length * mat[0].length != r * c) return mat;
        int[][] res = new int[r][c];
        int a = 0, b = 0;
        for(int i=0; i<mat.length;i++){
            for(int j=0; j<mat[0].length;j++){
                res[a][b] = mat[i][j];
                if(b+1==c){
                    b = 0;
                    a += 1;
                }
                else b += 1;
            }
        }
        return res;
    }
}
