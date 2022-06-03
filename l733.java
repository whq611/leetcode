public class l733 {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int a = image[sr][sc];
        if(a==newColor) return image;
        return dfs(image, sr, sc, a, newColor);
    }

    public int[][] dfs(int[][] image, int sr, int sc, int a, int newColor){
        if( 0<=sr && sr<image.length && 0<=sc && sc<image[0].length && image[sr][sc] == a){
            image[sr][sc] = newColor;
            dfs(image, sr-1, sc, a, newColor);
            dfs(image, sr+1, sc, a, newColor);
            dfs(image, sr, sc-1, a, newColor);
            dfs(image, sr, sc+1, a, newColor);
            
        }
        return image;
    } 
}
