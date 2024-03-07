class Solution {

    boolean visited[][];
    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;
        visited = new boolean[rows][cols];
        
        if(word.length() == 0){return false;}
        for(int r=0; r<rows; r++){
            for(int c=0; c<cols; c++){
                if(word.charAt(0) == board[r][c]){
                    if(search(r, c, word, board, 0)){return true;}
                }
            }
        }
        return false;
    }

    public boolean search(int r, int c, String word, char[][] board,int k){

        if(k == word.length()){return true;}

        if(r >= board.length || r < 0 || c >= board[0].length || c < 0 || visited[r][c] || board[r][c] != word.charAt(k)){return false;}

        visited[r][c] = true;

        if(board[r][c] == word.charAt(k)){
            if (search(r+1, c, word, board, k+1) || search(r-1, c, word, board, k+1)
            || search(r, c+1, word, board, k+1) || search(r, c-1, word, board, k+1) ){
                return true;
            }
        }

        visited[r][c] = false;
        return false;
    }
}