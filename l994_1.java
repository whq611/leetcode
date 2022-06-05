public class l994_1 {
    int[][] grid;
    public int orangesRotting(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }

        this.grid = grid;    
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 2) {
                    dfs(i, j, 2); // 开始传染
                } 
            }
        }

        // 经过dfs后，grid数组中记录了每个橘子被传染时的路径长度，找出最大的长度即为腐烂全部橘子所用的时间。
        int maxLevel = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    return -1; // 若有新鲜橘子未被传染到，直接返回-1
                } else {
                    maxLevel = Math.max(maxLevel, grid[i][j]);
                }
            }
        }

        return maxLevel == 0? 0: maxLevel - 2; 
    }

    private void dfs(int i, int j, int level) { // level用来记录传染路径的长度（当然最后要减2）
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length ) {
            return;
        }
        if (grid[i][j] != 1 && grid[i][j] < level) { // 只有新鲜橘子或者传播路径比当前路径长的橘子，才继续进行传播。
            return;
        } 
   
        grid[i][j] = level; // 将传染路径的长度存到grid[i][j]中
        level++;
        dfs(i - 1, j, level);
        dfs(i + 1, j, level);
        dfs(i, j - 1, level);
        dfs(i, j + 1, level);
    }
}
