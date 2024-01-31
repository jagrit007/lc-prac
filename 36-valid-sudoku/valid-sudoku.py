import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        box = set()
        for i, _row in enumerate(board):
            for j, _col in enumerate(_row):
                row_num = _row[j]
                col_num = board[j][i]
                box_num = board[3 * math.floor(i/3) + math.floor(j/3)][ ((i*3)%9) + (j%3)]
                if row_num != '.':
                    if row_num not in col:
                        col.add(row_num)
                    else:
                        return False
                if col_num != '.':
                    if col_num not in row:
                        row.add(col_num)
                    else:
                        return False
                if box_num != '.':
                    if box_num not in box:
                        box.add(box_num)
                    else:
                        return False
            row=set()
            col=set()
            box=set()
        return True

