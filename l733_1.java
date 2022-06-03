import java.util.LinkedList;
import java.util.List;

public class l733_1 {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int a = image[sr][sc];
        if(a==newColor) return image;
        return bfs(image, sr, sc, a, newColor);
    }

    public int[][] bfs(int[][] image, int sr, int sc, int a, int newColor){
        LinkedList<int[]> stack = new LinkedList<>();
        stack.add(new int[] {sr,sc});
        while(!stack.isEmpty()){
            int[] b = stack.removeFirst();
            if( 0<=b[0] && b[0]<image.length && 0<=b[1] && b[1]<image[0].length && image[b[0]][b[1]] == a){
            image[b[0]][b[1]] = newColor;
            stack.add(new int[] {b[0]-1,b[1]});
            stack.add(new int[] {b[0]+1,b[1]});
            stack.add(new int[] {b[0],b[1]-1});
            stack.add(new int[] {b[0],b[1]+1});
            
        }
        }
        return image;
        
    }
}
