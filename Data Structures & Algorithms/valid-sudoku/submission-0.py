class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical_count = {}
        square = {}
        for i in range(0,9):
            x_axis = i//3
            horizontal_count = {}
            for j in range(0,9):
                y_axis = j //3
                if board[i][j] != ".":
                    horizontal_count[board[i][j]] = horizontal_count.get(board[i][j], 0) + 1
                    square[(x_axis, y_axis)] = square.get((x_axis, y_axis), {})
                    square[(x_axis, y_axis)][board[i][j]] = square[(x_axis, y_axis)].get(board[i][j],0)+1
                    if horizontal_count[board[i][j]] > 1:
                        return False
                    
                    if square[(x_axis, y_axis)][board[i][j]]  > 1:
                        return False
                    
                if board[j][i] != ".":
                    vertical_count[board[j][i]] = vertical_count.get(board[j][i], 0) + 1
                    if vertical_count[board[j][i]] > 1:
                        return False
            vertical_count = {}
        return True