class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> set = new HashSet<String>();
        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[i].length; j++){
                char num = board[i][j];
                if (num == '.') continue;
                if(!set.add(num + " row:" + i ) || !set.add(num + " col:" + j) || !set.add(num + " box:" + i/3 + " " + j/3)) return false;
            }
        }
        return true;
    }
}