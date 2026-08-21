class Spreadsheet:

    def __init__(self, rows: int):
        self.matrix = [[0] * 26 for i in range(rows)]
        self.labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def setCell(self, cell: str, value: int) -> None:
        col, row = self.labels.index(cell[0]), int(cell[1:len(cell)])-1
        self.matrix[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = self.labels.index(cell[0]), int(cell[1:len(cell)])-1
        self.matrix[row][col] = 0

    def getValue(self, formula: str) -> int:
        left, right = formula[1:formula.index("+")], formula[formula.index("+")+1:]
        ans = 0

        if left[0] in self.labels:
            ans += self.matrix[int(left[1:]) - 1][self.labels.index(left[0])]
        else:
            ans += int(left)
        
        if right[0] in self.labels:
            ans += self.matrix[int(right[1:]) - 1][self.labels.index(right[0])]
        else:
            ans += int(right)

        return ans

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
