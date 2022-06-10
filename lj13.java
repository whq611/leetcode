public class lj13 {
    public int movingCount(int m, int n, int k) {
        int[][] visited = new int[m][n];
        return dfs(0,0,m,n,k,visited);
    }

    private int dfs(int i, int j, int m, int n, int k, int[][] visited){
        if (i < 0 || i >= m || j < 0 || j >= n || get(i)+get(j) > k || visited[i][j]==1) {
            return 0;
        }
        visited[i][j] = 1;
        return dfs(i + 1, j, m, n, k, visited) + dfs(i - 1, j, m, n, k, visited) + 
               dfs(i, j + 1, m, n, k, visited) + dfs(i, j - 1, m, n, k, visited) + 1;

    }

    private int get(int x) {
        int res = 0;
        while (x != 0) {
            res += x % 10;
            x /= 10;
        }
        return res;
    }
}
