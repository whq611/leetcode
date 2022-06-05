import java.util.LinkedList;
import java.util.Queue;

public class l994 {
    public int orangesRotting(int[][] grid) {
        int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Queue<int[]> queue = new LinkedList<int[]>();
        int count = 0, minute = 0;
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                }
                if (grid[i][j] == 1) {
                    count += 1;
                }
            }
        }
        if(count==0) return 0;
        while(!queue.isEmpty()){
            int l = queue.size();
            for(int i=0; i<l; i++){
                int[] node = queue.poll();
                for(int[] d: dir){
                    int x = node[0]+d[0];
                    int y = node[1]+d[1];
                    if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y]==1) {
                    grid[x][y] = 2;
                    queue.offer(new int[]{x, y});
                    
                }
                }
            }
            minute += 1;
        }
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }
        return minute - 1;
    }
}
