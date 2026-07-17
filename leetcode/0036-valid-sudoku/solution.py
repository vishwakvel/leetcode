class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                if num == ".":
                    continue
                
                if num in rows[i] or num in cols[j] or num in squares[(i//3, j//3)]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                squares[(i//3,j//3)].add(num)
        
        return True
