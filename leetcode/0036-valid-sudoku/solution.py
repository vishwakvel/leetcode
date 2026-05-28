class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. For each row, column, and 3x3 box, have a defaultdict with the default value being an empty set and the keys are i and j (row/col numbers)
        2. Iterate through every single square
            a) If its a "." continue
            b) Check if the number in that square is already in any of the dicts
                a) If it is, return False
                b) If not, add the key value pair (index: value) to each of the dicts
        3. If it goes through iteration fully, then it passed the tests so return True
        """

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                box = (i // 3, j // 3)

                if (val in rows[i] or val in cols[j] or val in boxes[box]):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box].add(val)
        
        return True
