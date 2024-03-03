class Solution {
    public boolean isSafe(char[][] board, int row, int col, int number){
        //column and row
        for(int j=0; j<board.length; j++){
            if((char)(number + '0') == board[row][j]){return false;}
            if((char)(number + '0') == board[j][col]){return false;}
        }

        //3x3 grid
        int startingRow = 3*(row/3);
        int startingCol = 3*(col/3);

        for(int i=startingRow; i < startingRow + 3; i++){
            for(int j=startingCol; j < startingCol + 3; j++){
                if((char)(number + '0') == board[i][j]){return false;}
            }
        }

        return true;
    }
    public boolean helper(char[][] board, int row, int col){
        if(row == board.length){
            return true;
        }
        // for next recursive call
        int new_row = 0;
        int new_col = 0;
        if (col != board.length - 1){
            new_row = row;
            new_col = col + 1;
        }
        else {
            new_row = row + 1;
            new_col = 0;
        }

        if(board[row][col] != '.'){
            if( helper(board, new_row, new_col) ) {return true;}
        }
        else{
            for(int i=1; i<=9; i++){
                if(isSafe(board, row, col, i)){
                    board[row][col] = (char) (i + '0');
                    if(helper(board, new_row, new_col)){
                        return true;
                    } else{
                        board[row][col] = '.';
                    }
                }
            }
        }
        return false;
    }
    public void solveSudoku(char[][] board) {
        helper(board, 0, 0);
    }
}