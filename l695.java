public class l695 {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j]==1) res = Math.max(res,dfs(grid,i,j));
            }
        }
        return res;
    }

    public int dfs(int[][] grid, int i, int j){
        int k = 0;
        if(i>=0 && i<grid.length && j>=0 && j<grid[0].length && grid[i][j]==1){
            grid[i][j] = 0;
            k += 1;
            k += dfs(grid,i-1,j);
            k += dfs(grid,i+1,j);
            k += dfs(grid,i,j-1);
            k += dfs(grid,i,j+1);
            return k;
        }
        else return 0;
    }
}
