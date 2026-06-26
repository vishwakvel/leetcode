class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(row, col, index):
            if index == len(word):
                return True

            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != word[index]):
                return False
            
            char = board[row][col]
            board[row][col] = "#"

            found = backtrack(row + 1, col, index + 1) or backtrack(row - 1, col, index + 1) or backtrack(row, col + 1, index + 1) or backtrack(row, col - 1, index + 1)

            board[row][col] = char
            return found

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True

        return False
