public class lj12 {
    public boolean exist(char[][] board, String word) {
        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[0].length; j++){
                if(board[i][j]==word.charAt(0)){
                    boolean a = dfs(i,j,board,word,0);
                    if(a==true) return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(int i, int j, char[][] board, String word, int k){
        if(i >= board.length || i < 0 || j >= board[0].length || j < 0 || board[i][j] != word.charAt(k)) return false;
        if(k == word.length() - 1) return true;
        board[i][j] = '\0';
        boolean res = dfs( i + 1, j, board, word, k + 1) || dfs(i - 1, j, board, word, k + 1) || 
                      dfs(i, j + 1, board, word, k + 1) || dfs(i , j - 1, board, word, k + 1);
        board[i][j] = word.charAt(k);
        return res;


    }
}
