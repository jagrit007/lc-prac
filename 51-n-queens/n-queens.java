// TC: O(n^n)
class Solution {
    public void saveBoard(List<List<String>> allBoards, char board[][]){
        String row = "";
        List<String> newBoard = new ArrayList<>();
        for(int i=0; i<board.length; i++){
            row = "";
            for(int j=0; j<board[0].length; j++){
                if(board[i][j] == 'Q'){
                    row += 'Q';
                }
                else{
                    row += '.';
                }
            }
            newBoard.add(row);
        }
        allBoards.add(newBoard);
    }

    public boolean isSafe(char board[][], int row, int col){
        // column
        for(int j=0; j<board.length; j++){
            if(board[row][j] == 'Q'){
                return false;
            }
        }

        // row
        for(int i=0; i<board[0].length; i++){
            if(board[i][col] == 'Q'){
                return false;
            }
        }

        // upper left row-- col--
        int r = row;
        for(int c=col; c>=0 && r>=0; c--, r--){
            if(board[r][c] == 'Q'){
                return false;
            }
        }

        // uper right c++ r--
        r = row;
        for(int c=col; c<board.length && r>=0; c++, r--){
            if(board[r][c] == 'Q'){
                return false;
            }
        }

        // lower left r++ c--
        r = row;
        for(int c=col; c>=0 && r<board.length; c--, r++){
            if(board[r][c] == 'Q'){
                return false;
            }
        }

        // lower right r++ c++
        r = row;
        for(int c = col; c<board.length && r<board.length; c++, r++){
            if(board[r][c] == 'Q'){
                return false;
            }
        }

    return true;
    }

    public void helper(List<List<String>> allBoards, char board[][], int col){
        if (col == board.length){
            saveBoard(allBoards, board);
            return; 
        }
        for(int row=0; row<board.length; row++){
            if(isSafe(board, row, col)){
                board[row][col] = 'Q';
                helper(allBoards, board, col+1);
                board[row][col] = '.';
            }
        }
    }
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> allBoards = new ArrayList<>();
        char board[][] = new char[n][n];
        helper(allBoards, board, 0);
        return allBoards;
    }
}