class Solution:
    def __init__(self):
        self.board = None

        self.rowDotsCount = None
        self.rowSet = None

        self.colDotsCount = None
        self.colSet = None

        self.squDotsCount = None
        self.squSet = None

        self.next = None

    def equal(self):
        # row
        rowRes = self.rowDotsCount + len(self.rowSet) == 9
        self.rowDotsCount = 0
        self.rowSet = set()
        if not rowRes:
            return False

        # column
        colRes = self.colDotsCount + len(self.colSet) == 9
        self.colDotsCount = 0
        self.colSet = set()
        if not colRes:
            return False

        # square
        sqrRes = self.squDotsCount + len(self.squSet) == 9
        self.squDotsCount = 0
        self.squSet = set()
        if not sqrRes:
            return False

        return True

    def doCalculate(self, i, rowAndColumnIndent, boardIndex, squareIndent, leftSide, rightSide):
        # row
        if self.board[self.next][i - rowAndColumnIndent] == ".":
            self.rowDotsCount += 1
        else:
            self.rowSet.add(self.board[self.next][i - rowAndColumnIndent])

        # column
        if self.board[i - rowAndColumnIndent][self.next] == ".":
            self.colDotsCount += 1
        else:
            self.colSet.add(self.board[i - rowAndColumnIndent][self.next])

        # square
        if i < 9:  # handle "0 < 0 < rightSide - 6" problem
            if i < 3:
                if self.board[boardIndex][i - squareIndent] == ".":
                    self.squDotsCount += 1
                else:
                    self.squSet.add(self.board[boardIndex][i])
            if 2 < i < 6:
                if self.board[boardIndex + 1][i - squareIndent - 3] == ".":
                    self.squDotsCount += 1
                else:
                    self.squSet.add(self.board[boardIndex + 1][i - 3])
            if 5 < i < 9:
                if self.board[boardIndex + 2][i - squareIndent - 6] == ".":
                    self.squDotsCount += 1
                else:
                    self.squSet.add(self.board[boardIndex + 2][i - 6])

        else:
            if leftSide < i < rightSide - 6:
                if self.board[boardIndex][i - squareIndent] == ".":
                    self.squDotsCount += 1
                else:
                    self.squSet.add(self.board[boardIndex][i - squareIndent])
            if leftSide + 3 < i < rightSide - 3:
                if self.board[boardIndex + 1][i - squareIndent - 3] == ".":
                    self.squDotsCount += 1
                else:
                    self.squSet.add(self.board[boardIndex + 1][i - squareIndent - 3])
            if leftSide + 6 < i < rightSide:
                if self.board[boardIndex + 2][i - squareIndent - 6] == ".":
                    self.squDotsCount += 1
                else:
                    self.squSet.add(self.board[boardIndex + 2][i - squareIndent - 6])

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        self.board = board

        self.rowDotsCount = 0
        self.rowSet = set()

        self.colDotsCount = 0
        self.colSet = set()

        self.squDotsCount = 0
        self.squSet = set()

        self.next = 0

        for i in range(82):
            if i != 0 and i % 9 == 0:
                self.next += 1

            # ============================================

            if i < 9:
                self.doCalculate(i, 0, 0, 0, 0, 9)

            if i == 9:
                if not self.equal():
                    return False

            # ============================================

            if 8 < i < 18:
                self.doCalculate(i, 9, 0, 6, 8, 18)

            if i == 18:
                if not self.equal():
                    return False

            # ============================================

            if 17 < i < 27:
                self.doCalculate(i, 18, 0, 12, 17, 27)

            if i == 27:
                if not self.equal():
                    return False

            # ============================================

            if 26 < i < 36:
                self.doCalculate(i, 27, 3, 27, 26, 36)

            if i == 36:
                if not self.equal():
                    return False

            # ============================================

            if 35 < i < 45:
                self.doCalculate(i, 36, 3, 33, 35, 45)

            if i == 45:
                if not self.equal():
                    return False

            # ============================================

            if 44 < i < 54:
                self.doCalculate(i, 45, 3, 39, 44, 54)

            if i == 54:
                if not self.equal():
                    return False

            # ============================================

            if 53 < i < 63:
                self.doCalculate(i, 54, 6, 54, 53, 63)

            if i == 63:
                if not self.equal():
                    return False

            # ============================================

            if 62 < i < 72:
                self.doCalculate(i, 63, 6, 60, 62, 72)

            if i == 72:
                if not self.equal():
                    return False

            # ============================================

            if 71 < i < 81:
                self.doCalculate(i, 72, 6, 66, 71, 81)

            if i == 81:
                if not self.equal():
                    return False

        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "."],
    ["4", ".", ".", "8", ".", "3", ".", ".", "."],
    ["7", ".", ".", ".", "2", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "5"],
    [".", ".", ".", ".", ".", ".", ".", "7", "9"]
]
s = Solution()
print(s.isValidSudoku(board))
