import java.util.HashSet;

public class l36 {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character>[] rows = new HashSet[9];
        HashSet<Character>[] cols = new HashSet[9];
        HashSet<Character>[] boxs = new HashSet[9];
        for(int i=0;i<9;i++){
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxs[i] = new HashSet<>();
        }
        for(int r=0;r<9;r++){
            for(int c=0;c<9;c++){
                char val = board[r][c];
                if(val=='.') continue;
                if(rows[r].contains(val) || cols[c].contains(val) || boxs[r/3*3+c/3].contains(val)) return false;
                rows[r].add(val);
                cols[c].add(val);
                boxs[r/3*3+c/3].add(val);
            }
        }
        return true;
    }
}
