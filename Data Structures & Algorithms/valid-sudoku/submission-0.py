class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # go through each entry by row, but keep track of columns and
        #   cubes by lists of maps

        # find if entry is in column by going through each row for j=1..9
        # find if entry is in 'cell' by looking at i and j (int(i/3)+int(j/3))

        rows: list[set[str]] = [set() for i in range(9)]
        cols: list[set[str]] = [set() for i in range(9)]
        cells: list[set[str]] = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                cell_idx = int(i / 3) + 3*int(j / 3)
        
                if (board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in cells[cell_idx]):
                    return False

                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    cells[cell_idx].add(board[i][j])

        return True




        