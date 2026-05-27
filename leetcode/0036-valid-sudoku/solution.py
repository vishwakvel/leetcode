class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        3 Parts
        1. For each row, have a set where u check first if number already in set before adding to it
            a) If it is then false
            b) If it isn't then add and continue
        2. Same process for columns as well
        3. For the 3x3 box, defaultdict for each box (r//3, c//3) and the values are a set of all the numbers and you check before adding a number if that number is already in value
            a) If it is then false
            b) If it isn't then add and continue
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
