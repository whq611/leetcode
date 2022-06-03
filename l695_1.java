import java.util.LinkedList;

public class l695_1 {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j]==1) res = Math.max(res,bfs(grid,i,j));
            }
        }
        return res;
    }

    public int bfs(int[][] grid, int i, int j){
        int k = 0;
        LinkedList<int[]> stack = new LinkedList<>();
        stack.add(new int[] {i,j});

        while(!stack.isEmpty()){
            int[] b = stack.removeFirst();
            if(b[0]>=0 && b[0]<grid.length && b[1]>=0 && b[1]<grid[0].length && grid[b[0]][b[1]]==1){
            grid[b[0]][b[1]] = 0;
            k += 1;
            stack.add(new int[] {b[0]-1,b[1]});
            stack.add(new int[] {b[0]+1,b[1]});
            stack.add(new int[] {b[0],b[1]-1});
            stack.add(new int[] {b[0],b[1]+1});
        }
        }
        return k;
        
    }
}
