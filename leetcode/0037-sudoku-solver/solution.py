class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i // 3) * 3 + (j // 3)].add(board[i][j])

        def backtrack(index):
            if index == len(empty):
                return True

            r, c = empty[index]
            b = (r // 3) * 3 + (c // 3)

            for num in (set("123456789") - rows[r] - cols[c] - boxes[b]) :
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if backtrack(index + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

            return False

        backtrack(0)
