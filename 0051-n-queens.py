class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()

        board = [["."] * n for i in range(n)]
        ans = []

        def backtrack(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if (col in cols or (row - col) in diag1 or (row + col) in diag2):
                    continue
                
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row][col] = "."
            
        backtrack(0)
        return ans
